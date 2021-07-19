from .models import Task
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(CreateView):
    #we send post request , therefor we need to create an item
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    model = Task 
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')