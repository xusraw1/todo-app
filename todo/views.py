from django.views.generic import ListView, DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLogin(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todo/homepage.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False)
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'todo/detail.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'todo/create.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'todo/create.html'
    success_url = reverse_lazy('list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('list')
