import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime

# TJ 노래방 차트 크롤링
url = 'https://www.tjmedia.com/tjsong/song_monthPopular.asp?strType=1'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
table_body = soup.select_one('div#wrap div#body div#contents div div div#BoardType1 table.board_type1 tbody')

chart = []
for tr in table_body.find_all('tr')[1:]:
    rank = tr.find_all('td')[0].text.strip()
    song_number = tr.find_all('td')[1].text.strip()
    song_title = tr.find_all('td')[2].text.strip()
    artist = tr.find_all('td')[3].text.strip()
    chart.append((song_title, artist))

# 스포티파이 API 연결
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='👇',
    client_secret='👇',
    redirect_uri='http://localhost:8080',
    scope='playlist-modify-public'
))
user = sp.current_user()['id']

# 플레이리스트 찾기 또는 생성
playlists = sp.user_playlists(user)
playlist_id = None
for playlist in playlists['items']:
    if playlist['name'] == 'TJ 노래방 인기차트 ＴＯＰ１００ TJ Karaoke Charts':
        playlist_id = playlist['id']
        break

if playlist_id is None:
    playlist = sp.user_playlist_create(user, 'TJ 노래방 인기차트 ＴＯＰ１００ TJ Karaoke Charts')
    playlist_id = playlist['id']

# 플레이리스트에서 모든 노래 제거
sp.playlist_replace_items(playlist_id, [])
print('플레이리스트에서 모든 노래 제거 완료')

# 블랙리스트와 대체 제목 로드
blacklist = set()
with open('blacklist.txt', 'r') as f:
    for line in f:
        song, artist = line.strip().split(' * ')
        blacklist.add((song, artist))

replace_dict = {}
with open('replace.txt', 'r', encoding='utf-8') as f:
    for line in f:
        melon_name, other_name = line.strip().split(' * ')
        replace_dict[melon_name] = other_name

log_file = open('log.txt', 'w')

# TJ 노래를 스포티파이에 검색하고 플레이리스트에 추가
for title, artist in chart:
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
        if (track['name'], ", ".join(artists)) in blacklist:
            log_file.write(f'\n{spotify_song} 해당 노래는 블랙리스트에 등록이 되어있어 다음 검색결과로 넘어갔습니다.\n\n')
            print(f'{spotify_song}의 노래 이름이 블랙리스트에 있어서 그 다음 검색결과로 넘어갑니다.')
            continue

        sp.playlist_add_items(playlist_id, [track['id']])
        log_file.write(f'TJ Karaoke: \"{title}\", TJ Artist: \"{artist}\", Spotify: {spotify_song}, Spotify ID: {track["id"]}\n')
        print(f'플레이리스트에 성공적으로 추가되었습니다. TJ 노래방: \"{title}\" / 스포티파이: {spotify_song} 노래가 추가되었습니다!')
        break

current_time = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분에 자동 갱신됨")
emoji_string = "💕 플레이리스트 하트 한번씩 눌러주세용~ 💕 - ⏰ " + current_time + " ⏰ - ⚠️ 오류가 있을 수 있습니다. 문의는 디스코드 \"yuuuubi\" 로 해주세용~ ⚠️"
sp.playlist_change_details(playlist_id, description=emoji_string)

log_file.write(datetime.now().strftime("\n" + "%Y년 %m월 %d일 %H시 %M분에 자동 갱신 완료됨") + "\n")
log_file.close()
