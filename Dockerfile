FROM jenkins/jenkins:lts
WORKDIR /usr/src/app
COPY . .
WORKDIR /var/jenkins_home/workspace/educolab_back/backend
RUN venv/bin/pip install -r requirements.txt
RUN source venv/bin/activate
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "educolab.wsgi:application"]
# EXPOSE 8000
