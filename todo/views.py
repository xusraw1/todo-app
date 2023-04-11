from django.views.generic import ListView
from .models import Task


# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'todo/homepage.html'
    context_object_name = 'tasks'
