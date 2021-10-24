rm -R db.sqlite3
rm -r restify/migrations/*
touch restify/migrations/__init__.py
python manage.py makemigrations
python manage.py migrate
DJANGO_SUPERUSER_PASSWORD=Joseph@22 python manage.py createsuperuser --username ashields --email admin@email.com --noinput
