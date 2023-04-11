from django.views.generic import ListView, DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'todo/homepage.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    template_name = 'todo/detail.html'


class TaskCreate(CreateView):
    model = Task
    template_name = 'todo/create.html'
    fields = '__all__'
    success_url = reverse_lazy('list')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'todo/create.html'
    success_url = reverse_lazy('list')


class TaskDelete(DeleteView):
    model = Task
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('list')
