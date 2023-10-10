from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.login_and_user_info, name='login_and_user_info'),
]
