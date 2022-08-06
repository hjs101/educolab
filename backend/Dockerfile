FROM jenkins/jenkins:lts
RUN mkdir /code
WORKDIR /code 
ADD requirements.txt /code/
RUN pip install -r requirements.txt 
ADD . /code/