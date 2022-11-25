#  EduColab ( 교육과 기술의 청량한 조화! )
<img src="/uploads/85e4097f8177ffa87cc5b0dd1a7df106/educolab.37f5cd03.png" width="250">

### UCC : [링크](https://youtu.be/ESee2Ut4Xcg)

### 시연 시나리오 : [링크](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102/-/blob/master/exec/%EC%8B%9C%EC%97%B0%20%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4.md)

## ✨Overview
1. 수업에 도움을 주는 서비스! : 교사는 설문조사를 통해 수업을 개선, 퀴즈와 과제 기능을 수업에 활용!

2. 학습 욕구를 고취시키는 서비스! : 포인트 상점을 위해 의욕이 상승하고 퀴즈, 자율학습 등의 기능을 이용하여 학습 효과 UP!

## 팀 소개 : 광주 1반 C102 정신이 들어...? Team

Frontend : 나원경, 정석호
Backend : 한진성, 홍찬기
Embeded : 여동준, 이국희

## 핵심 서비스

### 설문조사 등록
![선생_013_설문조사_등록](/uploads/1dd1b65146c0f9b696f1ac4dca000f9a/선생_013_설문조사_등록.gif)

### 설문조사 제출
![학생_임베디드__003_설문조사_제출](/uploads/be5d1c289a81ddc4b8c20fea8b30a2a5/학생_임베디드__003_설문조사_제출.gif)

### 설문조사 통계
![선생_017_설문조사_통계](/uploads/275cf0fd357a5e5410a5f66a44090d3e/선생_017_설문조사_통계.gif)

### 과제 등록
![선생_005_과제_등록](/uploads/ae6174c6390b86dd22d4d0b6b300cb06/선생_005_과제_등록.gif)

### 과제 제출
![학생_004_과제_제출](/uploads/d3c93c60a3e82bcc1e6cd7f975e7326a/학생_004_과제_제출.gif)

### 과제 채점
![선생_006_과제_채점](/uploads/dc331e6614f9369e357abefbc14f92c4/선생_006_과제_채점.gif)

![선생_007_과제_채점2](/uploads/03f0de57631ceecc38a1a66f6c1b5a05/선생_007_과제_채점2.gif)

### 퀴즈
![공통_001_퀴즈](/uploads/540e196e0cf7d82b91c4579988c5bcca/공통_001_퀴즈.gif)

### 포인트 상점
![학생_007_포인트상점](/uploads/87ac0201dce594e06aff43b0b792887e/학생_007_포인트상점.gif)

## ✨ 주요 기능
---
- 서비스 설명 : 스마트 기기를 활용하여 교사와 학생 사이의 수업 전달력을 높이고, 학생의 자기주도학습을 보조하는 학습 플랫폼
- 주요 기능 :
    - 설문조사 등록(Web) 및 제출(Embed), 통계 기능을 통한 수업 개선
    - 과제를 부여하고 제출받아 채점할 수 있는 과제 기능
    - IOT 기기 이용하여 참여할 수 있는 실시간 퀴즈 시스템
    - 상/벌점을 두고, 상점을 이용해 칭호, 뱃지를 구매할 수 있는 포인트 상점 기능

### 개발 환경

---

**Backend**
- Visual Studio Code
- pyton 3.9.5
- Django 3.2.12
- simple jwt
- AWS EC2
- mysql
- redis

**Frontend**

- Visual Studio Code
- Vue.js 3.2.13
- Quasar 2.0.0
- vuex 4.0.2
- node.js 16.16.0


**Embeded**

- Raspberry Pi
   HW : Raspberry Pi 4 Model B Rev 1.2
   SW : Raspbian GNU/Linux 11 (bullseye)
- python 3.9.2
- Kivy 2.1.0
- websocket-client : 1.3.3
- mysql-connector-python: 8.0.30
- requests: 2.28.1

**CI/CD**
- aws ec2
- docker
- nginx
- jenkins

###각 개발 환경 별 포팅 매뉴얼

Frontend : [링크](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102/-/blob/master/front-end/README.md)

Backend : [링크](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102/-/blob/master/backend/README.MD)

Embeded : [링크](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102/-/blob/master/embedded/README.md)

### 아키텍쳐 구성도

---

![아키텍쳐 구성도](/uploads/a1a8362d2e4b2565ec68fb7a3f6177ec/Image_Pasted_at_2022-8-15_22-31.png)

### Jenkins를 이용한 CD 구축 및 SSL 인증서 적용

---

백엔드 CICD 배포 및 SSL 인증서 적용 과정은 [여기](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102/-/blob/master/CICD.md)에서 설명해두었습니다.

### 특이점

---

- Kivy

라즈베리파이의 성능이 기존의 태블릿보다 떨어지기 때문에, 웹을 사용하면 라즈베리파이의 성능상 속도가 매우 느려질 거라고 생각했습니다. 라즈베리 파이에서 사용할 수 있는 App을 구현하는 것을 목표로했고, 관련해서 App 제작을 위한 디자인 툴을 찾아보았습니다. Pyqt는 디자인적으로 부족한 점이 있었고, 그 외 여러 후보군 들 중 Kivy가 원하는 디자인을 만들 수 있다고 판단하여 Kivy를 이용하여 App을 제작하였습니다.

- Quasar : Vue3에서 현재 Vue bootstap이 적용이 안되는 상황에서, Vue3에 특화되어있는 디자인 툴이었기 때문에 사용했습니다. pagenation, modal 등 css만으로는 구현하기 어려운 내용들을 간단하게 구현할 수 있는 컴포넌트들이 많아서, 이를 이용하여 화면을 구성하였습니다.

- Redis

실시간 퀴즈 기능을 구현할 때, 소켓 프로그래밍을 이용하여 웹 -> 임베디드로 신호를 보내어 퀴즈 시작시간을 동기화 하는 방법을 생각했습니다. 이러한 통신을 Django에서 사용하기 위해서는 Redis를 이용해야 한다는 것을 알게 되었고, 도커 컨테이너에 추가하여 Django와 연동했습니다.

- Django-channels

소켓 통신을 위해서 처음에는 파이썬 Websocket 라이브러리를 사용하여 구현을 할 생각이었습니다. 하지만 초기 구현을 진행할 때 막막함이 앞섰고, 개발 전에 장고에서 제공하는 웹 소켓 통신 기능이 있지 않을까 싶어 찾아보던 와중 Django channels를 찾게 되었습니다. Django-channels는 장고의 프로젝트 구조와 유사한 방식으로 소켓 통신을 구현할 수 있도록 지원해줍니다. 이를 이용하여 웹 소켓을 이용한 실시간 퀴즈 기능을 구현하였습니다.

- 배포

Docker, Nginx, Jenkins를 이용하여 무중단 자동 배포를 구축하였습니다. Nginx는 Aws에 서버를 띄워 FE를 서비스했고, Django 서버는 도커의 컨테이너로 넣어 AWS EC2의 Nginx에 도커 프록시로 연결했습니다.



### 협업

---
- Git
- Jira
- Notion
- Mattermost
- Webex
- discode

### 기능 정의서

---
![기능_정의서_1](/uploads/ca30c9aa7193e1a2656f5aa5013e497b/기능_정의서_1.jpg)

![기능_정의서_2](/uploads/c611b84956c82e61dd148eeee7d20392/기능_정의서_2.jpg)

![기능_정의서_3](/uploads/4d89e9feeaa9207aafce54efb568dbc1/기능_정의서_3.jpg)


### 화면 정의서

---

화면 정의서는 [여기](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102/-/blob/master/outputs/%ED%99%94%EB%A9%B4_%EC%A0%95%EC%9D%98%EC%84%9C.pdf)에서 확인해주시기 바랍니다.


### ✨Git 컨벤션

---

```
# <Type> : <제목> 형식으로 작성
# <Type> 영문으로 첫글자 대문자 지켜서 작성
# <제목> 한글로 작성, 제목 끝에 마침표 금지. 무엇을 했는지 1줄로 작성.
#####제목#####

##############
# 아래 공백은 제목과 본문의 분리를 위해 유지

# 본문(추가 설명)이 있는 경우 작성
# 본문은 '어떻게'보다는 '무엇을', '왜' 했는지 설명하기
#####본문#####

##############
# 꼬릿말(footer)을 작성 (관련된 이슈 번호 등 추가)
# 아래 공백은 본문과 꼬릿말의 분리를 위해 유지

# Resolves : 해결 issue
# See also : 참조 및 관련 issue
# 예시) Jira 이슈 S07P12C102-39 해결시 아래와 같이 작성
# Resolves : #39
#####꼬리말#####

#####Type#######
# Feat     : 새로운 기능 추가
# Fix      : 버그 수정
# Docs     : 문서 수정
# Test     : 테스트 코드 추가
# Refactor : 코드 리팩토링
# Style    : 코드 의미에 영향을 주지 않는 변경사항
# Chore    : 빌드 부분 혹은 패키지 매니저 수정사항
################

```

###  ER Diagram

---

![ERD](/uploads/53e58cf572132880d670c9944203a78b/image.png)

- ERD입니다.

### Sequence Diagram

시퀀스 다이어그램은 [여기](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102/-/blob/master/outputs/Sequence%20Diagram.docx)에서 확인하세요!
