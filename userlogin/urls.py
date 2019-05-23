from django.urls import path

from . import views

app_name = 'userlogin'
urlpatterns=[
    path('register', views.register,name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('', views.index, name='index'),
    path('special', views.special, name='special'),
    path('logout', views.logout, name='logout')
]