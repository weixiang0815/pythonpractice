from django.urls import path

from . import views

app_names = "polls"
urlpatterns = [
    path("", views.index, name="index")
]