# django_project 협업 시나리오

멤버 : 송호석(개발자A) , 김병석(개발자B)

1. 최초 구성
개발자 A가 장고 프로젝트를 생성 하고 관련한 모든 설정 들을
docker image로 빌드하여 컨테이너를 실행시켜본다.
로컬에서 http://127.0.0.1:8000/ 포트로 접속시 장고 기본 화면이 나온다면 성공
docker 이미지는 dockerhub에 푸시하고 장고프로젝트는 github에 푸시한다.

2. 협업시나리오
개발자 B는 github에서 소스를 내려 받는다.
프로젝트 폴더의 root 경로에서 (즉 docker-compose.yml 파일이 있는 경로)
docker-compose up -d 명령어를 통해 이미지를 빌드하고 컨테이너를 생성 -> 실행 한다.

docker-compose ps 명령어로 컨테이너가 실행 중 인지를 확인하거나
직접 http://127.0.0.1:8000/ 으로 접속해 장고가 실행중인지 확인한다.

정상적으로 실행중이라면 Docker Desktop 앱은 종료 해도 된다. ( 메모리 많이 잡아 먹음 )

이제부터 개발자 B는 개발을 시작하고 변경된 소스 코드 내용을 github에 푸시한다.
소스코드가 변경될때마다 사이트에 자동으로 반영된다.
docker-compose up -d ( 백그라운드로 컨테이너가 실행중이기 때문 )

Dockerfile 내용을 수정 했다면
docker-compose up -d --build 명령어를 통해
이미지를 재 build 하고 해당 이미지를 docker hub에 푸시 한다.

만약 라이브러리를 새롭게 추가해야 되는 상황이 생긴다면
ex) pip install requests 

로컬에서 라이브러리(패키지)를 설치하게 되면 freeze 명령어로
방금 받은 라이브러리를 requirements.txt 에 기록 해야 한다.
ex) pip freeze > requirements.txt
