# rm -R db.sqlite3
rm -r restify/migrations/*
rm -r rufus/migrations/*
rm -r funkify/migrations/*
rm -r funkifymorphic/migrations/*
touch restify/migrations/__init__.py
touch rufus/migrations/__init__.py
touch funkify/migrations/__init__.py
touch funkifymorphic/migrations/__init__.py
python manage.py makemigrations
python manage.py migrate
DJANGO_SUPERUSER_PASSWORD=Joseph@22 python manage.py createsuperuser --username ashields --email admin@email.com --noinput
