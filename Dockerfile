FROM python:3.8.6
ENV PYTHONUNBUFFERED 1
WORKDIR /web
COPY . .
RUN pip install -r requirements.txt