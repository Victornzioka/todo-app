from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib import messages


from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from django.contrib.auth.models import User
from .forms import RegisterForm


from .models import TodoList
from .forms import TodoListForm


# Create your views here.
class TodoListView(LoginRequiredMixin, ListView):
    model = TodoList
    context_object_name = 'tasks'

    #  ------------------------overwride the get_context_data list with our custom data--------------   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context

class TodoDetailView(LoginRequiredMixin, DetailView):
    model = TodoList

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = TodoList
    form_class = TodoListForm
    # fields = ['task', 'details', 'complete']
    success_url = reverse_lazy('todo-list')

    # ----------------assign each task to the logged in user---------------------
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)

class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = TodoList
    form_class = TodoListForm
    success_url = reverse_lazy('todo-list')

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoList
    success_url = reverse_lazy('todo-list')

class LoginView(LoginView):
    template_name = 'todo_app/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo-list')
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))



class RegisterView(FormView):
    template_name = 'todo_app/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo-list')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        
        return super(RegisterView, self).form_valid(form)