import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

from cache_celery.celery import app
from .models import DummyData


@shared_task
def create_random_user_account(total):
    for i in range(total):
        username = 'user_{}'.format(
            get_random_string(10, string.ascii_letters))
        email = '{}@{}.com'.format(username, username)
        password = get_random_string(50)
        User.objects.create_user(
            username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)


@shared_task
def create_random_people():
    for i in range(10):
        name = '{} {}'.format(
            get_random_string(10, string.ascii_letters),
            get_random_string(10, string.ascii_letters))
        age = get_random_string(2, string.digits)
        DummyData.objects.create(name=name, age=age)
    return '10 random people created with success!'


@app.task(name="delete_all_users", bind=True, default_retry_delay=300, max_retries=3)
def delete_all_users(self):
    try:
        all_users = User.objects.all().exclude(username='abdullah')
        for user in all_users:
            user.delete()
    except:
        delete_all_users.retry()

    return f'All users ({all_users.count()}) deleted with success!'


@app.task(name="delete_all_people", bind=True, default_retry_delay=300, max_retries=3)
def delete_all_people(self):
    try:
        all_people = DummyData.objects.all()
        for person in all_people:
            person.delete()
    except:
        delete_all_people.retry()

    return f'All people ({all_people.count()}) deleted with success!'
