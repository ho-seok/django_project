docker-compose 기본적으로 사용하는 명령어

#컨테이너 생성 및 실행
docker-compose up
#백그라운드에서 실행
docker-compose up -d
#이미지 빌드부터 컨테이너 생성 및 실행
docker-compose up --build

#컨테이너 정지 및 이미지 일괄삭제
docker-compose down --rmi all
#커스텀 태그가 없는 이미지만 삭제
docker-compose down --rmi local

#컨테이너 확인
docker-compose ps
#컨테이너 ID만 확인
docker-compose ps -q
#컨테이너 로그 확인
docker-compose logs
#컨테이너 내에서 임의로 명령어 실행
docker-compose run 컨테이너명 /bin/bash

#컨테이너 시작/정지/재시작
docker-compose start
docker-compose stop
docker-compose restart

#컨테이너 접속 방법
#컨테이너 ID확인
docker ps
#컨테이너 접속
docker exec -it 컨테이너 ID /bin/bash 
