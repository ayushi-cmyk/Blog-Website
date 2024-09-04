from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("<int:id>", views.view_details, name="view_details"),
]