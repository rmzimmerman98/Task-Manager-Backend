from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks', views.TaskList.as_view(), name='task_list'),
    path('api/tasks/<int:pk>', views.TaskList.as_view(), name='task_detail'),
]