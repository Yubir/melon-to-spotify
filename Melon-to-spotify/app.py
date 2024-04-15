from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime

# 멜론사이트 크롤링 후 정보 변수로 저장하기
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


def is_song_in_blacklist(song, blacklist):
    return song in blacklist


# 스포티파이 API 불러오기 ( 사용하는 방법은 README 참고 )
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='👇',
    client_secret='👇',
    redirect_uri='http://localhost:8080',
    scope='playlist-modify-public'
))

user = sp.current_user()['id']

# 계정에 해당 플레이리스트가 있는지 확인하고 없으면 새로 만들기 ( 이 기능은 처음 사용하는 사람을 위해 만듦 )
playlists = sp.user_playlists(user)
playlist_id = None
for playlist in playlists['items']:
    if playlist['name'] == '자동화 멜론차트 ＴＯＰ１００ Melon Charts':
        playlist_id = playlist['id']
        break

if playlist_id is None:
    playlist = sp.user_playlist_create(user, '자동화 멜론차트 ＴＯＰ１００ Melon Charts')
    playlist_id = playlist['id']

# 플레이리스트에 추가하기 전 플레이리스트에서 모든 노래 제거
sp.playlist_replace_items(playlist_id, [])
print('플레이리스트 모든 노래 제거 완료')

blacklist = set()
with open('blacklist.txt', 'r') as f:
    for line in f:
        song, artist = line.strip().split(' * ')
        blacklist.add((song, artist))

log_file = open('log.txt', 'w')

# 멜론노래를 스포티파이에 검색할땐 다른 노래로 검색하기
replace_dict = {}
with open('replace.txt', 'r', encoding='utf-8') as f:
    for line in f:
        melon_name, other_name = line.strip().split(' * ')
        replace_dict[melon_name] = other_name

# 크롤링한 멜론 차트 노래를 스포티파이에 검색하고 플레이리스트에 추가하기
for title, artist in chart:
    # 노래 제목이 replace.txt에 있다면, 대체 제목으로 검색
    if title in replace_dict:
        search_title = replace_dict[title]
        log_file.write(f'\n\"{title}\" 해당 노래는 Replace.txt에 등록되어 있기 때문에 \"{search_title}\" 으로 검색되었습니다.\n\n')
        print(f'\"{title}\"의 노래가 대체되어 \"{search_title}\"로 검색되었습니다.')
    else:
        search_title = title

    results = sp.search(f'{search_title}', type='track')

    for track in results['tracks']['items']:
        artists = [a['name'] for a in track['artists']]
        spotify_song = f'\"{", ".join(artists)}\"의 \"{track["name"]}\"'
        skipped_song = f'\"{artist}\"의 \"{title}\"'
        if (track['name'], ", ".join(artists)) in blacklist:
            log_file.write(f'\n{spotify_song} 해당 노래는 블랙리스트에 등록이 되어있어 다음 검색결과로 넘어갔습니다.\n\n')
            print(f'{spotify_song}의 노래 이름이 블랙리스트에 있어서 그 다음 검색결과로 넘어갑니다.')
            continue

        sp.playlist_add_items(playlist_id, [track['id']])

        log_file.write(f'Melon: \"{title}\", Melon Artist: \"{artist}\", Spotify: {spotify_song}, Spotify ID: {track["id"]}\n')
        print(f'플레이리스트에 성공적으로 추가되었습니다. 멜론: \"{title}\" / 스포티파이: {spotify_song} 노래가 추가되었습니다!')
        break
current_time = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분에 자동 갱신됨")
emoji_string = "💕 플레이리스트 하트 한번씩 눌러주세용~ 💕 - ⏰ " + current_time + " ⏰ - ⚠️ 오류가 있을 수 있습니다. 문의는 디스코드 \"yuuuubi\" 로 해주세용~ ⚠️"
sp.playlist_change_details(playlist_id, description=emoji_string)

log_file.write(datetime.now().strftime("\n" + "%Y년 %m월 %d일 %H시 %M분에 자동 갱신 완료됨") + "\n")
log_file.close()