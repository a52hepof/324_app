#!/usr/bin/env bash
# exit on error
set -o errexit
pip install -r requeriments.txt
#python manage.py makemigrations
python manage.py collectstatic --no-input
#python3 manage.py collectstatic --no-input
python manage.py migrate
#python3 manage.py migrate

#create superusers. Primer despliegue 
#python manage.py createsuperuser --noinput #take enviroment variables
#python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('324', 'admin@example.com', '1')"

#Funciona perfectamente
#python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('324', 'admin@example.com', '1')"