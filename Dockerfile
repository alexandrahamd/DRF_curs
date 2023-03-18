FROM python:3

EXPOSE 8080

WORKDIR /code

RUN pip install --upgrade pip
RUN pip install django
RUN pip install celery
RUN pip install django-celery-beat
RUN pip install djangorestframework
RUN pip install djangorestframework-simplejwt
RUN pip install drf-yasg
RUN pip install Pillow
RUN pip install psycopg2
RUN pip install python-dotenv
RUN pip install redis
RUN pip install requests
RUN pip install psycopg2-binary

COPY . .

CMD python manage.py runserver 0.0.0.0:8080