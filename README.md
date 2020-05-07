# 수정중

### 프로젝트 요약
- 소개: [폴바셋](https://www.baristapaulbassett.co.kr/Index.pb) 웹사이트 클론
- 기간: 2020.04.20 - 2020.05.01 (약 2주)
- 인원: 프론트엔드 2명([MJ Kim](https://github.com/howdy-mj),  [skh417](https://github.com/skh417)), 백엔드 2명([ikswary](https://github.com/ikswary), [Magrfs](https://github.com/Magrfs))
- Frontend-Repo: [PaulBa3-frontend](https://github.com/wecode-bootcamp-korea/PaulBa3-frontend)

----

### 데모
- 클릭 시 데모 영상으로 이동

[![메인](https://media.vlpt.us/images/magnoliarfsit/post/eb955457-4c79-4474-b8ba-2f99c9378da4/mainpage.png)](https://www.youtube.com/watch?v=a1vKyWHA8pE&feature=youtu.be)

----

### 사용된 기술
- **Frontend**: JavaScript, React.js, SASS
- **Backend**: Python, Django, Selenium, BeautifulSoup4, MySQL
- **Deployment**: AWS EC2

----

### 구현 기능
**Sign-up**:
- 아이디 중복 확인 및 유효성 검사 구현
- 회원가입 시 필수정보(아이디, 비밀번호, 이름, 생일, 전화번호)에 대한 유효성 검사 구현
- 회원가입 시 비밀번호 암호화 (Bcrypt)

**Sign-in**:
- 로그인 실패 시 에러코드 반환
- 로그인 성공 시 JWT를 통한 토큰 생성 및 프론트엔드에 전달

**Store**:
- 시/도를 클릭 시 해당하는 구/군의 이름과 코드, 그리고 지역 매장수에 따라 clickable true/false 를 반환

**Store-Detail**:
- 지역구 클릭 시 해당 지역구에 존재하는 모든 지점들의 정보를 반환

**Product-Summary**:
- 메뉴 소개 페이지에 사용되는 product의 이름, img를 반환
- 카테고리별로 각각의 코드를 매핑하여 구현

**Product-Detail**:
- 메뉴 소개 페이지에서 클릭했을 때 나타나는 상세 설명 페이지에 사용되는 정보들을 반환

----

### API Documentation (with POSTMAN)
[백엔드 API](https://wecode-baulba3.postman.co/collections/10870734-52c1a3b7-9745-415f-af93-efba995b0d7b?version=latest&workspace=3529cce5-1706-4ef4-8bc9-d3b75531384b)

----

### 데이터 모델링 (with AqueryTool)
![Aquery](https://images.velog.io/images/ikswary/post/b8f57721-ab90-43f0-83aa-832f50b1b5e5/paulbassett_20200507_48_12.png)

