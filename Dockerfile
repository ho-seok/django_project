# docker hub에 존재하는 ubuntu 16.04 버전의 이미지를 base로 사용
FROM ubuntu:18.04
 
# 우분투 기본 세팅
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa

# 파이썬 3.8 설치
RUN apt-get update
RUN apt install -y python3.8
RUN apt install -y python3-pip
RUN apt install -y python3.8-dev libpq-dev
RUN apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

# # 파이썬 default version 3.5 -> 3.6 설정
# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
# RUN update-alternatives --config python3

# net-tools, dnsutils 설치
RUN apt-get install -y net-tools
RUN apt-get install -y dnsutils
RUN apt-get update
 
# 파이썬 출력 버퍼 제거
ENV PYTHONUNBUFFERED 0

# 작업 디렉토리를 아래와 같이 설정
WORKDIR /home/django_project
 
# requirements.txt 설치
COPY requirements.txt /home/django_project
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# postgres를 위한 대기 스크립트, 추후에 설명
#ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /