web: gunicorn --chdir api/ --env DJANGO_SETTINGS_MODULE=config.settings config.wsgi
release: python api/manage.py migrate
