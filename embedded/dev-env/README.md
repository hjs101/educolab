# 개발 환경 세팅

#### Contens

1. 라즈베리 파이 초기화
2. 라즈베리 파이 kivy 설치

### 1. 라즈베리파이 초기화

#### SD 카드 포맷 & PI Imager 다운

#### wifi 세팅

#### 연결 : SPI, I2C, VNC. ssh

<br>

### 2. 라즈베리 파이 kivy 설치

#### 참고자료 <br>

- 공식사이트 : https://kivy.org/doc/stable/installation/installation-rpi.html?highlight=apt%20get<br>
- 블로그 : https://blog.daum.net/recoo/5245981

#### 설치 코드<br>

- 정확한 Dependency는 확인되지 않음. 설치시 kiby 예제 실행됨<br>

```
$sudo apt update
$sudo apt install python3-setuptools git-core python3-dev
$sudo apt install pkg-config libgl1-mesa-dev libgles2-mesa-dev libgstreamer1.0-dev \
 gstreamer1.0-plugins-{bad,base,good,ugly} gstreamer1.0-{omx,alsa} libmtdev-dev xclip \
 xsel libjpeg-dev
$sudo apt-get install python3-pygame python3-opengl build-essential python3-pip
$sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
$sudo pip install kivy
```

#### 예제 파일

- **example01.py** : 화면 중앙에 화면 종료 버튼
