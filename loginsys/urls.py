from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('signup/', views.signup),
    path('profile/<int:user_id>/', views.profile),
]
