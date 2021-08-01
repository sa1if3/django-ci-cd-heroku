release: python manage.py makemigrations --noinput && python manage.py migrate --noinput
web: gunicorn django_ci_cd_heroku.wsgi --log-file -