from django.urls import path
from . import views

urlpatterns = [
    path("", views.inde, name="index_view"),
]
