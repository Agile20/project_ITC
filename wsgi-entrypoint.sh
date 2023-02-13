#!/bin/sh

until cd /app/
do
    echo 'Waiting for server volume...'
done

python manage.py makemigrations --no-input

until ./manage.py migrate
do 
    echo 'Waiting for db to be ready...'
    sleep 2
done


./manage.py collectstatic --noinput

gunicorn core.wsgi --bind 0.0.0.0:2000 --workers 4 --threads 4

