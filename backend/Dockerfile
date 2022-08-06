FROM jenkins/jenkins:lts
WORKDIR /usr/src/app
COPY . .
WORKDIR /var/jenkins_home/workspace/educolab_back/backend
ADD requirements.txt
RUN pip install -r requirements.txt
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "educolab.wsgi:application"]
# EXPOSE 8000
