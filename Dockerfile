FROM jenkins/jenkins:lts
WORKDIR /usr/src/app
COPY . .
WORKDIR /var/jenkins_home/workspace/educolab_back/backend
RUN source venv/bin/activate
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "educolab.wsgi:application"]
# EXPOSE 8000
