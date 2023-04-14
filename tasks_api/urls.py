from django.urls import path
from . import views

urlpatterns = [
    path('api/task', views.TaskList.as_view(), name='task_list'),
    path('api/task/<int:pk>', views.TaskDetail.as_view(), name='task_detail'),
]