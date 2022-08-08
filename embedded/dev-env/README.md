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

```bash
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


### 3. 윈도우 kivy 설치
#### 현재 notebook python 버전 확인 <br>
윈도우 터미널
```bash
$python --version
```

#### 가상환경 설치 <br>
Rpi python version >> python 3.9.2 32-bit

#### python 설치  <br>
https://www.python.org/ 접속 
> Downloads > 3.9.2 > 아래로 내려서 Windows installer (32-bit) 설치 > customized version > 설치 경로 기록

#### 환경 변수 설정  <br>
>제어판 > 시스템> 고급 시스템 설정 > 환경변수 > path > 경로 추가 > 설치 경로 저장

만약 환경 변수 설정 후 파이썬 버전 체크시 기존 버전 정보가 아니라 3.9.2로 변경되었다면, 기존 버전 정보의 python을 찾아서 환경변수로 재등록하고 파이썬 3.9.2 보다 위로 이동시키기(우선순위 문제) <br>

#### 적절한 위치에 다음과 같이 실행 (powershell 기준) <br>
가상환경 설치 	`$py -3.9 -m venv [가상환경이름]` <br>
가상환경 실행 	`$.\[가상환경이름]\Scripts\activate` <br>
실행시 (가상환경이름) 경로> cmdline 형태로 실행되면 정상 작동
버전 체크시 정상적으로 변경된 것을 확인 가능 <br>
가상환경 종료	`$deactivate` <br>
 <br>

#### kivy 설치 <br>
가상환경 실행(activate)
```bash
$python -m pip install --upgrade pip setuptools
$python -m pip install "kivy[base]" kivy_examples
```

gitlab/embedded branch의 dev-env의 example01.py 활용 <br>
해당 파일이 있는 경로에서 아래와 같은 코드 실행시 화면 종료 버튼을 포함한 창이 등장하면 정상동작
```bash
$python example01.py
```