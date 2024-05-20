# 🎶 플레이리스트 보기
[<img src="img/Melon.png" width=150 />](https://open.spotify.com/playlist/20R8anptqFQTGk4P2X6dRp?si=e5098eae6e6645ea) [<img src="img/Tj.png" width=150 />](https://open.spotify.com/playlist/3lMWs2QjqGp3OuE6tV3zos?si=4991ce0e893344a5) [<img src="img/Tj-Jpop.png" width=150 />](https://open.spotify.com/playlist/4DtmAMcrMGFPOya57Vu4q2?si=bf62b9de6d404b14)
 
# 📢 공지
```
TJ 노래방 인기차트 플레이리스트하고 TJ JPOP 인기차트도 만들어졌어요! 좋아요 많이 눌러주세요~

20240520 스포티파이 차트 좋아요 1800개 감사합니다~
20240513 스포티파이 차트 좋아요 1600개 감사합니다!! 
20240506 스포티파이 차트 좋아요 1391개 감사합니다!! 곧 1400개 감사드립니다!
20240502 스포티파이 차트 좋아요 1240개 감사함다
20240428 스포티파이 차트 좋아요 1100개 감사합니다~
20240425 스포티파이 차트 좋아요 1000개 정말 진심으로 감사합니다!!!!!
20240421 스포티파이 멜론차트 좋아요 900개 달성 감사감사합니다!
```

# ❓ MELON TO SPOTIFY 란?
- **스포티파이에서도 멜론차트를 듣고싶어서 1인 개발한 멜론차트를 크롤링하여 자동화 플레이리스트를 만든 것 입니다.**

- 처음 MELON TO SPOTIFY 제작은 `2023년 7월 3월`달 계획되었지만 실제 운영 첫 운영 날짜는 `2024년 2월`달 부터 운영이 시작되었습니다.

1. :one: [플레이리스트 보기(클릭)](#🎶-플레이리스트-보기)
2. :two: [공지 확인하기(클릭)](#📢-공지)
3. :three: [업데이트 로그 (클릭)](#📋-업데이트-로그)
4. :four: [Blacklist.txt, Replace.txt 사용법 (클릭)](#🏷️-blacklisttxt와-replacetxt-사용법)
5. :five: [스포티파이 API 생성 방법 (클릭)](#👍-스포티파이-api-생성-방법)
6. :six: [이용 약관 (클릭)](#📜-약관)

# 📋 업데이트 로그
```
2024-04-16 - TJ 인기차트 , TJ 일본 곡 인기차트 플레이리스트 추가, 개발 완료
2024-03-20 - 멜론 자동화 차트 약간의 코드 개선
2024-02-XX - 멜론차트 자동화 첫 운영
2023-07-03 - 첫 레포 생성
```

# 🏷️ Blacklist.txt와 Replace.txt 사용법
```
(blacklist.txt)

<스포티파이 음악 이름> * <스포티파이 그 음악의 아티스트 명>

예시:
Queencard * (여자)아이들
```
```
(replace.txt)

<스포티파이에서 검색어로 바꿀 음악 이름> * <검색어로 바뀔 음악 이름>
* 즉 "ベテルギウス(ドラマ'SUPER RICH' OST)" 해당 음악을 스포티파이에서 "ベテルギウス" 으로 검색하도록 만드는 것.

예시:
ベテルギウス(ドラマ'SUPER RICH' OST) * ベテルギウス
```

# 👍 스포티파이 API 생성 방법
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

# <a id="terms"></a> 📜 약관
- [x] 불법 유포 절대 금지
- [x] 코드를 가져와 되 팔이 금지
- [x] 코드를 가져가거나 수정할때는 꼭 저를 언급하는 텍스트를 포함시켜주세요.
- [x] 이 코드가 문제되거나 코드 삭제 요청은 이메일로 연락주세요.
