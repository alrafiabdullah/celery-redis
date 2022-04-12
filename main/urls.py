from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users/list", views.users_list, name="users_list"),
    path("cache/test", views.cache_test, name="cache_test"),
    path("cache/time", views.get_cache_time, name="get_cache_time"),
]
