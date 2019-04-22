FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /mysite
WORKDIR /mysite
ADD requirements.txt /mysite/
RUN pip install -r requirements.txt
COPY ./mysite /mysite/
