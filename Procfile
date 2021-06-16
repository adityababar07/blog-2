release: python manage.py makemigrations && python manage.py migrate
web: gunicorn study_project.wsgi --log-file -