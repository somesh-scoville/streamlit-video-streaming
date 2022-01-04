FROM python:3.9

EXPOSE 8501

WORKDIR /usr/src

COPY requirements.txt ./

RUN pip install -r requirements.txt
