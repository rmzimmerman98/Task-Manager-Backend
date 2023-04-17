from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

# def task_detail(request, task_id):
#     task = Task.objects.get(id=task_id)
#     priority_display = task.get_priority_display() # Get the human-readable priority value
#     return render(request, 'task_detail.html', {'task': task, 'priority_display': priority_display})

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-priority')
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all().order_by('-priority')
    serializer_class = TaskSerializer

