from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.cache import cache

from .models import DummyData
from .tasks import create_random_user_account, create_random_people
from .form import GenerateRandomUserForm


# Create your views here.
def index(request):
    total_form = GenerateRandomUserForm(request.POST or None)
    if request.method == 'POST' and total_form.is_valid():
        total = total_form.cleaned_data['total']
        create_random_user_account.delay(total)
        total_form = GenerateRandomUserForm()
        messages.success(
            request, 'Your request has been submitted. Please wait a few minutes.')
        return redirect('users_list')

    context = {
        'total_form': total_form,
    }

    return render(request, "index.html", context=context)


def users_list(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, "user_list.html", context=context)


def cache_test(request):
    if request.method == "POST":
        create_random_people.delay()
        messages.success(
            request, 'Your request has been submitted. Please wait a few minutes.')
        return redirect('cache_test')

    if cache.get('people'):
        context = {
            "all_data": cache.get('people'),
            "hit": True,
            "ttl": cache.ttl('people'),
        }
    else:
        cache.set('people', DummyData.objects.all(), timeout=120)
        context = {
            "all_data": DummyData.objects.all(),
            "hit": False,
        }
    return render(request, "name_list.html", context=context)


def get_cache_time(request):
    return JsonResponse({"ttl": cache.ttl('people')}, status=200)
