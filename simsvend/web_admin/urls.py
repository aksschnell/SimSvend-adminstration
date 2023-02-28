from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("users", views.users, name="users"),
    path("login", views.login, name="login"),
    path("matches", views.matches, name="matches")
]
