from django.urls import path
from . import views
from .views import login

urlpatterns = [
    path('test/', views.test, name='test'),
    path('login/', views.login, name='login'),
]
