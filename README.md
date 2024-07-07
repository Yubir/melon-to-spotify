# 🎶 플레이리스트 보기
[<img src="img/Melon.png" width=150 />](https://open.spotify.com/playlist/20R8anptqFQTGk4P2X6dRp?si=e5098eae6e6645ea) [<img src="img/Tj.png" width=150 />](https://open.spotify.com/playlist/3lMWs2QjqGp3OuE6tV3zos?si=4991ce0e893344a5) [<img src="img/Tj-Jpop.png" width=150 />](https://open.spotify.com/playlist/4DtmAMcrMGFPOya57Vu4q2?si=bf62b9de6d404b14)
 
# 📢 공지
```
TJ 노래방 인기차트 플레이리스트하고 TJ JPOP 인기차트도 만들어졌어요! 좋아요 많이 눌러주세요~

20240707 스포티파이 차트 좋아요 3000개 달성!!!!!!!!!!!!!!!!!!!!!!!!!
20240526 스포티파이 차트 좋아요 2000개 감사합니다~
20240425 스포티파이 차트 좋아요 1000개 정말 진심으로 감사합니다!!!!!
```

# ❓ MELON TO SPOTIFY 란?
- **스포티파이에서도 멜론차트를 듣고싶어서 1인 개발한 멜론차트를 크롤링하여 자동화 플레이리스트를 만든 것 입니다.**

- 처음 MELON TO SPOTIFY 제작은 `2023년 7월 3월`달 계획되었지만 실제 운영 첫 운영 날짜는 `2024년 2월`달 부터 운영이 시작되었습니다.

1. :one: [플레이리스트 보기(클릭)](#🎶-플레이리스트-보기)
2. :two: [공지 확인하기(클릭)](#📢-공지)
3. :three: [업데이트 로그 (클릭)](#📋-업데이트-로그)
4. :four: [Blacklist.txt, Replace.txt 사용법 (클릭)](#🏷️-blacklisttxt와-replacetxt-사용법)
5. :five: [환경 변수 (클릭)](#⚙️-환경-변수)
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

# ⚙️ 환경 변수
## 필수 환경 변수
- ```SPOTIPY_CLIENT_ID```: Spotify 개발자 계정에서 발급받은 클라이언트 ID
- ```SPOTIPY_CLIENT_SECRET```: Spotify 개발자 계정에서 발급받은 클라이언트 시크릿

## 선택적 환경 변수
- ```SPOTIPY_REDIRECT_URI```: Spotify 인증 후 리디렉션될 URI (기본값: http://localhost:8080)

# <a id="terms"></a> 📜 약관
- [x] 불법 유포 절대 금지
- [x] 코드를 가져와 되 팔이 금지
- [x] 코드를 가져가거나 수정할때는 꼭 저를 언급하는 텍스트를 포함시켜주세요.
- [x] 이 코드가 문제되거나 코드 삭제 요청은 이메일로 연락주세요.
