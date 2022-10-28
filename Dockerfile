FROM ubuntu:latest
LABEL maintainer="asabhi6776"

ENV DEBIAN_FRONTEND=noninteractive \
    DJANGO_SETTINGS_MODULE=modupload.settings \
    DJANGO_DEBUG=True 

RUN apt-get update && \
    apt-get dist-upgrade --yes && \
	apt-get install -y libpng-dev libjpeg8-dev libfreetype6-dev libpq-dev python3-dev python3-pip libssl-dev libcurl4-openssl-dev git swig && \
	pip3 install --no-cache-dir --upgrade pyinotify && \
	apt-get autoremove -y && apt-get clean -y && \
	pip3 install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

ADD requirements.txt /root/src/modupload/requirements.txt
RUN export
RUN pip3 install -r /root/src/modupload/requirements.txt
COPY . /root/src/modupload/

ENTRYPOINT cd /root/src/modupload && \
            python3 manage.py collectstatic --noinput && \
            python3 manage.py makemigrations && \
            python3 manage.py migrate && \
            python3 manage.py runserver 0.0.0.0:9107

EXPOSE 9107
