# Commit Convention Template

### Contents

1. Commit Convention
2. Template 사용법

<br>

### 1. Commit Convention
- 협업시 코드 진행상황을 파악하기 위한 로그이자 약속
- 현재 프로젝트에서는 유명한 commit convention 가이드라인인 "Udacity git Commit Message Style Guide"를 참조.<br>

- 메시지 구조
```
Type : 제목

본문

꼬리말
```
- Type 종류<br>
`Feat` : 새로운 기능 추가<br>
`Fix` : 버그 수정<br>
`Docs` : 문서 수정<br>
`Test` : 테스트 코드 추가<br>
`Refactor` : 코드 리팩토링<br>
`Style` : 코드에 영향을 주지 않는 변경사항 <br>
`Chore` : 빌드 부분 혹은 패키지 매니저 수정사항 <br>
<br>

- 꼬리말<br>
Jira 이슈관리를 위해서 작성되는 부분<br>
`Resolves` : 해결된 issue 번호<br>
`See also` : 관련된 issue 번호
- 예시
```
Resolves : #123
See also : #456, #789
```
<br>

### 2. Template 사용법
본 가이드라인은 작성자가 Window terminal을 도구로 사용함에 따라 해당 기준으로 작성되었음.<br>
기존에 vim을 설치하거나, 다른 도구(ex. bash) 등을 사용하는 경우 적절히 건너뛰는 것을 추천함.<br>
처음 vim을 접한 경우 일부 명령어에 익숙해지는 것을 권장.<br>
<br>
<br>

**2-1. vim 설치**
- https://www.vim.org/download.php 접속
- PC:MS-DOS and MS-Windows 선택
- 최신버전 vim (gvim90.exe) 다운로드 및 설치
- Window terminal 혹은 powershell 재시작후 `$vim` 실행 확인
- 문제가 발생하는 경우 윈도우에서 '고급 시스템 설정 보기' > 환경변수 > path > vim 설치 위치 경로 등록 
<br>

**2-2. vim 단축 명령어 등록**
- 리눅스 사용자의 경우 vim보다 vi가 익숙하여 변경 과정이 필요한 경우가 있음
- Window terminal 기준 $profile에 저장된 경로에 직접 아래와 같이 입력하여 변경<br>
```
Set-Alias vi vim
```
- git bash 기준으로는 매번 시작시 source 파일을 실행하거나, git bash의 etc 폴더의 aliases.sh에 alias 명령어를 추가하는 방법이 있음(검증 미완료)
<br>

**2-3. Commit convention template 사용법 
- Gitlab, master branch에 업로드되어 있는 .gitmessage.txt 파일 다운로드
- home(~) 혹은 root(/)로부터 .gitmessage.txt 파일의 절대 경로 확인
- 다음 명령어 실행<br>
```
$git config --global commit.template <.gitmessage.txt의 절대 경로>
```
- commit 실행시 `$git commit`만 입력. 이후 vim으로 .gitmessage.txt의 내용 출력 확인
- 제시된 가이드라인(.gitmessage.txt)에 따라 Type, 제목, 본문, 꼬리말 작성
- 'a' 입력하여 vim 편집 상태로 전환
- `ESC` 이후 `:wq` 작성후 Enter
- 이후 일반적인 사용법과 같이 push 작업을 수행

