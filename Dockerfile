FROM python:3.10-slim
RUN apt-get update
WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')" | python manage.py shell
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
