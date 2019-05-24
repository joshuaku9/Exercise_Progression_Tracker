from django.urls import path

from . import views
from exercises.views import exercise_list

app_name = 'userlogin'
urlpatterns=[
    path('register', views.register,name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('', views.index, name='index'),
    path('special', views.special, name='special'),
    path('logout', views.user_logout, name='logout'),
    path('exercise_list', exercise_list, name='exercise_list'),
]