# Dockerfile
FROM jenkins:latest
USER root

RUN apt-get update

# pip 설치
RUN apt-get install -y python-pip
ENV JAVA_ARGS -Xms512m -Xmx1024m

RUN apt-get update && \
    apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget

# pyenv 설치/ 설정
RUN git clone https://github.com/pyenv/pyenv.git .pyenv
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# python v2, v3 설치
RUN pyenv install 3.10.5
RUN pyenv rehash