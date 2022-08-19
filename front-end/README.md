# front-end

## 목차



[간단한 기술 스택 소개](#기술-스택-및-패키지)

[프로젝트 설정](#프로젝트-설정)

[README 기본 내용](#README-기본-내용)

## 기술 스택 및 패키지

```
node.js 16.16.0   # 브라우저 내부에서 javascript 동작하기 위한 런타임 환경
Vue 3.2.13,   # Frontend Framework
Quasar 2.0.0,  # UI Framework
vuex 4.0.2,   # 중앙 저장소
vue-router 4.0.3  # router
dayjs: 1.11.5  # 날짜 데이터 출력
lodash: 4.17.21  # javascript에 없는 추가 함수 존재
```



## 프로젝트 설정

1. Node.js 설치

https://nodejs.org/ko/에서 Node.js 설치 (LTS 일정을 확인하고 LTS 버전을 설치하는 것을 추천)



2. vue cli 설치

```
npm install -g @vue/cli
```



3. vue 버전 확인

```
vue --version
```



4. vue 프로젝트 생성

아래 명령어를 실행해 프로젝트 폴더 안에 프로젝트가 생성

프로젝트 생성 시 vue-router와 vuex를 선택해 같이 설치해줌

```
vue create (프로젝트 폴더명)
```



5. vue 프로젝트 파일로 이동 후 실행

```
cd (프로젝트 폴더명)
npm run serve
```



6. 프로젝트 폴더 생성 후 vuex, vue-router 설치

router 설치 시 App.vue를 덮어쓰므로 App.vue 내용을 백업해둘 필요가 있음

```
vue add router
npm install vuex@next --save
```



7. 팀 작업을 할 때나 오류가 생겨 로컬 저장소를 초기화해야 할 때, git clone을 받은 후 프로젝트 설정하기

프로젝트에서 사용한 패키지를 설치 (사용된 패키지는 package.json, package-lock.json에 정리되어 있음)

```
npm install 또는 npm i
```



8. quasar  cli 설치

```
npm i -g @quasar/cli
npm init quasar
```



### 9. dayjs, lodash 설치

```
npm install dayjs --save
npm i --save lodash
```



## README 기본 내용

vue 프로젝트 생성 시 자동으로 생성된 README.md에 설명된 내용

## Project setup

```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
