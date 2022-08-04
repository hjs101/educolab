FROM sjoh0704/django:latest
WORKDIR /usr/src/app
COPY . .
WORKDIR ./backend
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000