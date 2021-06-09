FROM python:3.9.5-alpine
ENV PYTHONBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir /appsource
COPY ./appsource /appsource
WORKDIR /appsource
RUN adduser -D user
USER user
