from django.urls import path
from . import views

urlpatterns = [
    path('h/', views.receipes, name="get_post_res"), #receipes is funtion name#
    path("dr/<id>/", views.delete_res , name = "delete_res"),
    path("ur/<id>/", views.update_res , name = "update_res"),
]
