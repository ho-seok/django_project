# docker hub에 존재하는 ubuntu 16.04 버전의 이미지를 base로 사용
FROM python:3.8
 
# 파이썬 출력 버퍼 제거
ENV PYTHONUNBUFFERED 0

# 작업 디렉토리를 아래와 같이 설정
WORKDIR /home/
 
# requirements.txt 설치
COPY requirements.txt /home/
#RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# postgres를 위한 대기 스크립트, 추후에 설명
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /