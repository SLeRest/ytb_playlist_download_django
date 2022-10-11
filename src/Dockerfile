FROM ubuntu:22.04

# Setup timezone data
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get install -y apt-transport-https

# refresh package list
RUN apt-get update -y  --fix-missing
RUN apt-get clean
RUN apt-get upgrade -y
RUN apt-get install -y python3-dev python3-pip

# push all files needed
COPY manage.py /usr/src/manage.py
COPY app /usr/src/app
COPY ytb_playlist_download /usr/src/ytb_playlist_download
COPY requirements.txt /usr/src/requirements.txt
COPY entrypoint.sh /usr/src/entrypoint.sh
WORKDIR /usr/src

# install pip package
RUN pip3 install --upgrade pip
RUN --mount=type=cache,mode=0755,target=/root/.cache pip3 install -r ./requirements.txt

# let's go
ENTRYPOINT ["/usr/src/entrypoint.sh"]
