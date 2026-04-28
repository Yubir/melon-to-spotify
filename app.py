from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import schedule
import time
import os
from dotenv import load_dotenv
import logging

load_dotenv()

import sys, io

# 로그 설정
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logger = logging.getLogger('spotify_logger')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler(io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace'))
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def setup_file_logger():
    """spotify() 실행 시마다 새 로그 파일 생성"""
    # 기존 파일 핸들러 제거
    for handler in logger.handlers[:]:
        if isinstance(handler, logging.FileHandler):
            handler.close()
            logger.removeHandler(handler)
    
    log_file = os.path.join(log_dir, f'spotify_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log')
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def spotify():
    setup_file_logger()
    logger.info("자동 플리 시작")
    
    # 멜론사이트 크롤링
    url = "https://www.melon.com/chart/index.htm"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    chart = []
    for song in soup.select('.lst50, .lst100'):
        title = song.select_one('.ellipsis.rank01').text.strip()
        artist = song.select_one('.ellipsis.rank02').text.strip()
        chart.append((title, artist))

    logger.info(f"{len(chart)}개의 노래가 멜론차트에서 크롤링되었습니다.")

    # 스포티파이 API 불러오기
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
        scope='playlist-modify-public'
    ))

    user = sp.current_user()['id']
    logger.info(f"로그인되었습니다: {user}")

    # 환경 변수에서 플레이리스트 ID 가져오기
    playlist_id = os.getenv('SPOTIFY_PLAYLIST_ID')
    if not playlist_id:
        logger.error(".env 발견 안됨")
        return

    logger.info(f"해당 플리에 연결합니다: {playlist_id}")

    # 플레이리스트에 추가하기 전 플레이리스트에서 모든 노래 제거
    sp.playlist_replace_items(playlist_id, [])
    logger.info('플리에서 모든 노래를 삭제했습니다.')

    # blacklist와 replace 폴더 리스트로 변경
    blacklist = []
    with open('blacklist.txt', 'r') as f:
        for line in f:
            song, artist = line.strip().split(' * ')
            blacklist.append((song, artist))
    logger.info(f"{len(blacklist)}개의 blacklist 항목을 가져왔습니다.")

    replace_list = []
    with open('replace.txt', 'r', encoding='utf-8') as f:
        for line in f:
            melon_name, other_name = line.strip().split(' * ')
            replace_list.append((melon_name, other_name))
    logger.info(f"{len(replace_list)}개의 replace 항목을 가져왔습니다.")

    # 크롤링한 멜론 차트 노래를 스포티파이에 검색하고 플레이리스트에 추가하기
    for title, artist in chart:
        # 첫 번째로 매치되는 replace 항목 찾기
        search_title = next((other for melon, other in replace_list if melon == title), title)
        if search_title != title:
            logger.info(f' "{title}"가 "{search_title}"으로 대체되어 검색되었습니다.')

        results = sp.search(f'{search_title}', type='track')

        for track in results['tracks']['items']:
            artists = [a['name'] for a in track['artists']]
            spotify_song = f'"{", ".join(artists)}"의 "{track["name"]}"'
            
            # 첫 번째로 매치되는 blacklist 항목 찾기
            if any(b_song == track['name'] and b_artist == ", ".join(artists) for b_song, b_artist in blacklist):
                logger.info(f'{spotify_song} 이 노래는 블랙리스트입니다.')
                continue

            sp.playlist_add_items(playlist_id, [track['id']])
            logger.info(f'플리에 추가되었습니다 - Melon: "{title}" - "{artist}", Spotify: {spotify_song}')
            break

    current_time = datetime.now().strftime("%Y년 %m월 %d일 %H시에 자동 갱신됨")
    emoji_string = "⏰ " + current_time + " ⏰ 📌 매일 자정+1/정오에 업데이트됩니다."
    sp.playlist_change_details(playlist_id, description=emoji_string)
    logger.info("플리 설명 업데이트 완료")

    current_date = datetime.now().strftime("%y%m%d")
    playlist_name = f"⏰{current_date} 실시간 멜론차트 TOP 100 Melon Charts"
    sp.playlist_change_details(playlist_id, name=playlist_name)
    logger.info("플리 제목 업데이트 완료")

    logger.info("플리 업데이트 완료")

# 켜졌으니 한번 실행
spotify()

# spotify() # debug
schedule.every().day.at("12:00").do(spotify) # 매일 12시에 실행
schedule.every().day.at("00:00").do(spotify) # 매일 자정에 실행

logger.info("스케줄러 스타또!")

while True:
    schedule.run_pending()
    time.sleep(1)