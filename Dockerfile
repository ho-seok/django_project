#python 3.8.6 베이스 이미지
FROM python:3.8.6
#python 출력 버퍼 설정
ENV PYTHONUNBUFFERED 1
#작업 디렉토리
WORKDIR /web
#소스코드 복사
COPY . .
#파이썬 패키지 설치
RUN pip install -r requirements.txt