from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('advert/<int:advert_id>', views.advert),
]
