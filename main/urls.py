from django.contrib import admin
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.hello, name="hello"),
]
