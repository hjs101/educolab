FROM jenkins:lts
WORKDIR /usr/src/app
COPY . .
WORKDIR /var/jenkins_home/workspace/educolab_back/backend
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
