web: heroku run python ./manage.py collectstatic --noinput --settings=config.settings.heroku; gunicorn config.heroku_wsgi --settings=config.settings.heroku;