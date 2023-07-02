# 자동화 멜론차트 ＴＯＰ１００ Melon Charts 보러가기
**https://open.spotify.com/playlist/20R8anptqFQTGk4P2X6dRp?si=e5098eae6e6645ea**

![image](https://github.com/Yubir/melon-to-spotify/assets/101859341/b0308d97-ef17-4671-9329-4498c6d07507)

# Blacklist.txt 사용법
- blacklist.txt는 멜론차트 노래가 아닌 다른 노래가 검색됬을 경우를 대비하여 만들어놨습니다.
- 사용법은 간단합니다.
```
(blacklist.txt)

<스포티파이 음악 이름> * <스포티파이 그 음악의 아티스트 명>

Queencard * (여자)아이들
```
- 이렇게 적으시면 됩니다.
- 끝

# 스포티파이 API 생성 방법
- https://developer.spotify.com/dashboard 에 접속한다.
- ![image](https://github.com/Yubir/melon-to-spotify/assets/101859341/43f0a9ae-aaf1-4e33-9a3f-2922063cab8e)
- Create app 을 누른다.
- 자기 원하는대로 작성 후 마지막 Redirect URI 부분은 http://localhost:8080 로 한다.
- ![image](https://github.com/Yubir/melon-to-spotify/assets/101859341/707279e5-7264-4f71-ab1e-6e6e27727f64)
- Save를 누른 후 자기의 DASHBOARD에 들어간다.
- ![image](https://github.com/Yubir/melon-to-spotify/assets/101859341/881817fe-7f48-4b3f-a08f-5367c7e322f5)
- 들어가면 이런 모양인데 우측 상단에 Settings 버튼을 누른다.
- 그 후 View client secret 을 누른 후에
- ![image](https://github.com/Yubir/melon-to-spotify/assets/101859341/339c00cd-4005-495d-a327-64daf7aad35a)
- ![image](https://github.com/Yubir/melon-to-spotify/assets/101859341/31165b32-fcb5-461a-8bc6-9cd5ced17742)
- 둘 다 복사 한다.
- 그 뒤 app.py에 들어가서
- 32열에 client ID 를 적고
- 33열에 client SECRET 을 적는다.
- ![image](https://github.com/Yubir/melon-to-spotify/assets/101859341/521c4ec7-e87e-426b-a688-ab1b0f6b3d19)
- 그 후 코드를 실행하면...
- ![image](https://github.com/Yubir/melon-to-spotify/assets/101859341/43a83fcc-4327-4e90-be6e-9d25c788c4a5)
- 성공's



