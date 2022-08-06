FROM jenkins/jenkins:lts
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
WORKDIR /var/jenkins_home/workspace/educolab_back/backend
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "educolab.wsgi:application"]
EXPOSE 8000
