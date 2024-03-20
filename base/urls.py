from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path("", views.home, name="home"),
]