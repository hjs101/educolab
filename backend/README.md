# 포팅 매뉴얼 (CI,CD)

이 프로젝트의 CI/CD 및 배포 구성은 다음과 같다.

![구성도](/uploads/c70e6b8970e77da07069a5b2f1dcf235/Image_Pasted_at_2022-8-15_22-31.png)

1. Gitlab은 AWS 클라우드 EC2에 `WebHooks`로 연결되어 `Master Branch`가 갱신될 때마다 지정된 Build를 수행한다.
2. 젠킨스의 빌드 단계에서는 백엔드 서버 결과물(Django)을 Docker Image화 시켜 `DOCKER HUB`에 Push한다.
3. 이후, 빌드 후 조치로 프론트엔드 결과물(vue.js)을 Build하여 AWS 서버의 Nginx 배포 서비스 폴더에 복사하고, 도커 명령어를 통해 `DOCKER HUB`에 Push된 `image`를 내려받아 컨테이너로 배포한다. 이 때, django 서비스에 필요한 Redis 서버도 추가로 컨테이너로 추가한다.
4. Nginx에는 기본 프론트엔드 경로가 '/'으로, 백엔드 서버 경로를 '/api'로 경로를 구분하여, '/' 경로에는 front 빌드 파일이, '/api'에는 `Docker proxy`로 도커 내부 컨테이너에 연결한다.

### Jenkins Docker Container 설치

######docker-compose.yml
```
version: '3'

services:
    jenkins:
        image: jenkins/jenkins:lts
        container_name: jenkins_cicd
        volumes:
            - /var/run/docker.sock:/var/run/docker.sock
            - /jenkins:/var/jenkins_home
        ports:
            - "9090:8080"
        privileged: true
        user: root
```

DOCKER 컨테이너에 jenkins를 설치해준다. 포트는 임의의 사용자 포트를 사용한다. 보통 8080으로 설정되어있다.
image는 `jenkins/jenkins:lts`로, 젠킨스 컨테이너에서 docker 빌드를 사용하기 위한 `docker.sock`와 AWS 서버의 jenkins 폴더와 jenkins내부의 `jenkins_home` 폴더를 바인딩한다.

여기서는 vue.js 로컬에서 8080포트를 사용했기 때문에 입장 포트를 살짝 변경해주어 9090으로 설정해주었다.

위 파일을 AWS에 생성하고, `docker-compose up -d` 명령어를 통해 컨테이너를 실행시킨다.

컨테이너가 실행되었다면, AWS의 `Public IP:9090`으로 젠킨스에 접속이 가능하다.

![01](/uploads/6b40b9e8f11b4f107fe002b1665ce223/01.jpg)

젠킨스에 처음 접속하면 위와 같은 화면이 나타날 것이다. AWS 서버에서 위의 docker-compose.yml 파일이 있는 위치로 이동한다.

```
docker logs jenkins_cicd
```

위 명령어를 통해 젠킨스를 설치 할 때 생기는 비밀번호를 찾아 위 사진의 빈칸에 입력해줍니다.

![02](/uploads/5863dbee631a2ad3e968ea8fd098835e/02.jpg)

이후 기본으로 설치하라는 플러그인을 설치하고, 기본 설정할 admin 계정 정보를 세팅하면, Jenkins 설치가 끝이 난다.

### Jenkins, Gitlab
이제, Gitlab에서 설정한 Branch로 push를 하면 jenkins에서 자동으로 빌드를 실행하도록 설정해보자.

#### jenkins WebHooks

![03](/uploads/045b65abb5ed0e3596583bcd78aac29a/03.jpg)

먼저 Jenkins에서 플러그인 설치로 이동해 gitlab을 검색하고 다음 플러그인들을 설치한다.

![04](/uploads/cbfd8080ec5bdafca7974f15ae9694f4/04.jpg)

docker를 검색한 후 해당 플러그인들도 설치해준다.

![05](/uploads/9a019d4e47a289dca04f6a366f9b5900/05.jpg)

이제 젠킨스 메인화면으로 돌아와서 item을 한 개 생성한다. 타입으로는 FreeStyle Project를 선택해준다.

![06](/uploads/2ef950193ce2dede327954771f74ab20/06.jpg)

이후 소스코드 관리 탭에서, `Repositories` 에 프로젝트 url을, Credentials를 등록하여 추가해준다.

Credentials 등록 방법은 다음과 같다.

![07](/uploads/c318fab1ba2ab0badb4ac110a5d1c91e/07.jpg)

add -> jenkins 클릭

![08](/uploads/dcee76d4e70cf2392ace5e68b1cb3bbf/08.jpg)

username에 gitlab ID, Password에 gitlab PW, ID에 적당한 식별가능한 값을 넣어준다.

![06](/uploads/2ef950193ce2dede327954771f74ab20/06.jpg)

이 사진처럼 빨간색 에러 메시지가 안 뜨면 성공한 것이다.

![09](/uploads/310faed941d466b02581acfc7da1be53/09.jpg)

다음으로, 빌드 유발 탭에서 다음과 같이 설정해준다.

![10](/uploads/8296c7cb2601ef236c9238085e202851/10.jpg)

다음에는 추후 WebHooks를 설정할 Secret token 값을 따로 저장해 두도록 하자. 빌드 유발 탭에서 고급 버튼을 클릭한다.

![11](/uploads/58d0a794d2e890f3b0906d08f75768aa/11.jpg)

위 사진처럼 시크릿 토큰 칸이 있을텐데, `Generate` 버튼을 눌러 키를 생성하고 복사해둔다.

![12](/uploads/e9bf6f36b24b9924cbb3f838db24697c/12.jpg)

이후 Item을 생성하면 완료된다. 빌드 테스트를 위해 테스트 코드를 넣어보았다.


이제 `gitlab`에서 WebHooks 설정을 해줄 것이다.

![13](/uploads/acd27166a9ba0bf6e05ed35ed0b13779/13.jpg)

깃랩 프로젝트에서 위의 경로로 이동한다.

![14](/uploads/a8544ef03400e13d1385898c721acb51/14.jpg)

WebHooks를 이제 생성하도록 하자 위의 사진처럼 URL에는 `public IP OR URL:port/project/<item_name>`를 넣는다

Secret Token에는 아까 복사해두었던 토큰 값을 붙여넣기 하고,

그 아래의 Trigger에는 빌드를 유발하는 트리거 종류중 원하는 부분을 체크하면 된다.

![15](/uploads/a7b2f1f861379ed27423017e359863c6/15.jpg)

Master 브랜치에 Push 이후 자동으로 Build가 진행되는 모습이다.

### Django Build Setting

깃랩과 Jenkins 연결이 완료되었다. 이제 Dockerfile을 이용해 Django를 빌드해보자.

![16](/uploads/d0fa30788adf9ea78819cc362c1f1eb6/16.jpg)

일단 먼저 jenkins 컨테이너 안에 필요한 패키지들을 설치해준다. root 권한으로 jenkins 컨테이너에 접속한다.

```
apt-get update -y
apt-get install -y
apt-get install docker.io -y
apt-get install python3 pip -y
```

jenkins 컨테이너 안에서 다음 명령어들을 수행하여 설치를 진행해준다.

※ 우리 프로젝트의 경우 라이브러리 중 mysql-client를 설치하는데, ubuntu에서 그냥 해당 패키지를 설치하면 오류가 생긴다. 이에 대한 해결법은 다음과 같다.

```
# Debian, Ubuntu 계열
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

ubuntu에 해당 패키지를 설치해두면 mysql-client를 설치하는 데 오류가 발생하지 않을 것이다.

이제 DJango를 Build 하기 위한 준비가 끝났다.

### Docker 자동 빌드 및 DockerHub 업로드 설정

우선 프로젝트의 `Master Branch`에 빌드를 위한 Docker File이 있어야 한다.

dockerfile
```
FROM python:3.9.5
WORKDIR /var/jenkins_home/workspace/educolab_back/
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get -y update
RUN apt-get install -y redis-server
COPY . .
WORKDIR /var/jenkins_home/workspace/educolab_back/backend
```

Django 프로젝트 빌드를 위해 다음과 같이 도커 파일을 만들어주었다.

이후 Docker image 빌드 자동화 이후 Docker Hub에 업로드하도록 자동화시키는 쉘 스크립트를 만들었다. 출처 블로그를 참고했다.

```
#!/bin/bash

DOCKER_REPOSITORY_NAME=$1
ID=DOCKER_HUB_ID
PW=DOCKER_HUB_PW

#docker image의 첫 tag를 확인 후, 다음 버전의 image를 생성
#만약 처음 생성되는 이름이라면 0.01 이름으로 생성해준다.

TAG=$(docker images | awk -v DOCKER_REPOSITORY_NAME=$DOCKER_REPOSITORY_NAME '{if ($1 == DOCKER_REPOSITORY_NAME) print $2;}')

# 만약 [0-9]\.[0-9]{1,2} 으로 버전이 관리된 기존의 이미지 일 경우
if [[ $TAG =~ [0-9]\.[0-9]{1,2} ]]; then
    NEW_TAG_VER=$(echo $TAG 0.01 | awk '{print $1+$2}')
    echo "현재 버전은 $TAG 입니다."
    echo "새로운 버전은 $NEW_TAG_VER 입니다"

# 그 외 새롭게 만들거나, lastest or lts 등 tag 일 때
else
    # echo "새롭게 만들어진 이미지 입니다."
    NEW_TAG_VER=0.01
fi

# 현재 위치에 존재하는 DOCKER FILE을 사용하여 빌드
docker build -t $DOCKER_REPOSITORY_NAME:$NEW_TAG_VER .

# docker hub에 push 하기위해 login
docker login -u $ID -p $PW

if [ $NEW_TAG_VER != "0.01" ]; then
    docker rmi $DOCKER_REPOSITORY_NAME:$TAG
fi
# 새로운 태그를 설정한 image를 생성
docker tag $DOCKER_REPOSITORY_NAME:$NEW_TAG_VER $ID/$DOCKER_REPOSITORY_NAME:$NEW_TAG_VER

# docker hub에 push
docker push $ID/$DOCKER_REPOSITORY_NAME:$NEW_TAG_VER

# tag가 "latest"인 image를 최신 버전을 통해 생성
docker tag $DOCKER_REPOSITORY_NAME:$NEW_TAG_VER $ID/$DOCKER_REPOSITORY_NAME:latest

# latest를 docker hub에 push
docker push $ID/$DOCKER_REPOSITORY_NAME:latest

# 버전 관리에 문제가 있어 latest를 삭제
docker rmi $ID/$DOCKER_REPOSITORY_NAME:latest
docker rmi $ID/$DOCKER_REPOSITORY_NAME:$NEW_TAG_VER
```
해당 쉘 스크립트 파일은 jenkins 컨테이너 안의 적당한 위치에 적당한 파일명으로 생성하여 저장해두자. 여기서는 /var/jenkins_home/CICD/Docker_CD.sh로 저장했다.

`bash /var/jenkins_home/CICD/Docker_CD.sh "DOCKER HUB REPO NAME"`

위 명령어를 실행하면 Docker Hub에 설정된 계정으로 image가 업로드된다.

해당 명령어를 jenkins 빌드 옵션에 추가해야 한다.

![17](/uploads/370020985479cb3054b11c1f0d39a168/17.jpg)

젠킨스 item의 구성에서, Build 탭에 위 사진처럼 명령어를 추가해준다.

이제 젠킨스에서 빌드가 되면 설정한 Docker Hub 계정의 Repository에 빌드된 도커 image가 올라가게 된다.

### Docker Image 내려받아서 배포하기 + Nginx이용 퍼블릭 배포하기(FrontEnd + backend)

이제 Jenkins가 설치된 AWS에 SSH로 명령어를 보내 배포를 실행해볼 것이다.

![18](/uploads/4922407a2db1f13219bebc86304b03b9/18.jpg)

Jenkins에 해당 플러그인을 설치해준다.

![19](/uploads/88d8ac6c0d9b4fb2cc131ae78e17ce87/19.jpg)

jenkins 프로젝트의 구성에서, 빌드 후 조치 탭으로 이동하여, 빌드 후 조치 추가에 위 사진에 해당하는 항목(`Send build artifacts over SSH`)을 추가해준다.

![20](/uploads/32bd4bbb0119e848ccca438f10b8cda3/20.jpg)

최종적으로 빌드 후 조치 SSH 명령어는 다음과 같다.

빌드 테스트에 앞서 AWS EC2에 nginx 를 설치해보자

```
sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo apt install nginx
```

위 명령어를 사용하여 nginx 설치를 완료했다. 다음은 nginx에 Django 컨테이너와, Vue에서 build한 dist, nginx 서버를 연결해주도록 하자. 다음 파일은 nginx의 설정파일을 수정하여 Vue Build 파일, django 컨테이너를 연결할 것이다.

`/etc/nginx/sites-available/default` 파일을 vim 으로 열어보자, 설정된 파일 정보는 다음과 같다.

![21](/uploads/ac006d5871b8409e1c99c9f4f8f695b1/21.jpg)

![22](/uploads/d16cec1735d05449f7e42023d23490f1/22.jpg)

![23](/uploads/aef6809fa0b915b38bc074075463e2f5/23.jpg)

가려진 부분은 AWS public ip를 적으면 된다. HTTPS를 적용하려면 IP 대신 구매한 domain을 적으면 된다.

부가설명을 하자면, `location /api`를 통해 `/api`로 들어오는 요청은 도커 프록시로 연결되어있는 django 컨테이너 서버로 연결되고, `/`로 오는 요청은 nginx 서버로 연결이 되는데, 연결되는 base 폴더가 /var/www/html/dist이다. 이 폴더는 빌드 시 프로젝트 폴더에서 vue.js FE 프로젝트를 build해서 생긴 dist폴더를 그대로 옮긴 폴더이다.

그럼 이제 Docker proxy로 연결하는 Django 컨테이너를 생성해보자. 다시 젠킨스 container으로 접속해보자.

`docker exec -u 0 -it jenkins_cicd /bin/bash`

그 이후, jenkins_home의 wockspace, 프로젝트 명으로 접속하여 Django 서버 프로젝트 폴더로 이동한다. 여기서 경로는 다음과 같다.

`cd /var/jenkins_home/workspace/educolab_back/backend`

이 폴더에 docker-compose.yml 파일을 생성할 것이다. 생성한 docker-compose 파일은 다음과 같다.

```
version: "2"

services:
  django_web:
    image: h5282001/docker_educolab:latest
    container_name: django_web
    ports:
      - "8000:8000/tcp"
    command: daphne -b 0.0.0.0 -p 8000 educolab.asgi:application
    volumes:
      - ./static:/usr/src/app/staticfiles
      - ./media:/var/jenkins_home/workspace/educolab_back/backend/media

  redis:
    image: redis:latest
    ports:
      - "6379:6379"
    volumes:
      - ./redisdata:/data
```

h5282001은 `DockerHub id`이고, docker_educolab은 `DockerHub`에 저장한 `Repo` 이름이다.

장고는 그 자체 서비스로는 nginx에 연동할 수 없어 dephne를 통해 nginx에서 서비스 할 수 있게 변환하는 작업을 한다.

daphne를 통해 장고를 서비스하는 명령어가 `daphne -b 0.0.0.0 -p 8000 educolab.asgi:application` 이다.

또한 volumes를 통해 장고에서 제공하는 Static 파일들을 컨테이너 밖과 공유하도록 했다.

장고에서 소켓 프로그래밍을 사용할 때 도움이 되는 Redis도 함께 컨테이너로 추가를 해 주었다.

지금까지의 결과를 되돌아보자.

gitlab에서 FE, BE 프로젝트를 push하면, BE서버는 jenkins에서 `docker build`하여 DockerHub 에 업로드한다. 이후 원격 SSH 명령어를 통해 FE 파일은 Build 되어 /var/www/html/dist 에 저장이 되고, BE Django 서버는 Docker HUB에서 내려받아 컨테이너로써 서비스된다. 이 두 서버를 Nginx에서 location을 구분하여 웹 서비스가 이루어진다.

여기까지 진행함으로써 CICD 웹 서비스 배포가 완료되었다.

### https

웹 서비스 하면 빼놓을 수 없는게 https 적용이다. 여기서는 letsencrypt에서 인증서를 발급받아 https를 적용해보자.


먼저 Certbot를 설치한다.

```
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx
```

nginx 설정은 앞서 설정파일에 도메인이 적용이 되어있다.

이제 SSL 인증을 받아보자

`sudo certbot --nginx -d domain.com`

해당 명령어로 내 도메인에 대해 인증서를 받아올 수 있다.

```
Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
-------------------------------------------------------------------------------
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
-------------------------------------------------------------------------------
Select the appropriate number [1-2] then [enter] (press 'c' to cancel):
```

그러면 다음과 같은 안내메시지가 뜨는데, 2는 해당 도메인으로 오는 모든 http 요청을 https로 리다이렉팅 시키는 것이다.
1을 선택하면 https 요청이 아닌 요청은 리다이렉트 하지 않는다.

여기서 1, 2 선택까지 완료하면 https 적용도 완료가 된다.


[참고 출처 : jenkins를 사용한 DevOps 환경 구축](https://www.dongyeon1201.kr/9026133b-31be-4b58-bcc7-49abbe893044#c304d56a-fa56-4932-bdb0-076fa0bc5497)
[참고 출처 : nginx-lets-encrypt 무료로 https 설정하기](https://jp-hosting.jp/nginx-lets-encrypt%EB%A5%BC-%ED%86%B5%ED%95%B4-nginx%EC%97%90%EC%84%9C-%EB%AC%B4%EB%A3%8C%EB%A1%9C-https-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0/)
