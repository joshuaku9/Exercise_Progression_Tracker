from django.urls import path
from django.contrib import admin

from . import views

app_name = 'exercises'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.exercise_list, name='exercise_list'),
    path('create/', views.exercise_create, name='exercise_create'),
    path('edit/<int:pk>/', views.exercise_update, name='exercise_update'),
    path('delete/<int:pk>/', views.exercise_delete, name='exercise_delete'),
    path('graph/', views.exercise_graph, name='exercise_graph'),
]