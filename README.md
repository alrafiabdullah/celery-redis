# Celery Redis

##

## Requirements

- Install & run [Redis](https://redis.io/docs/getting-started/).
- Create and activate a virtual environment.
- Run `pip3 install -r requirements.txt`.
- Create a `secrets.json` file in the root directory with following content:

```
{
    "DJANGO_SECRET_KEY": ""
}
```

- Run `python3 manage.py migrate`.
- Run following commands simultaneously in different terminals:

  - Run `python3 manage.py runserver`.
  - Run `celery -A cache_celery.celery worker -l info`.
  - Run `celery -A cache_celery.celery beat -l info`.

- Run `python3 manage.py createsuperuser` and follow the prompts to create a superuser.

##
