from django.urls import path

from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView, LoginView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('tasks/', TodoListView.as_view(), name="todo-list"),
    path('task/<int:pk>', TodoDetailView.as_view(), name="todo-detail"),
    path('task/add_task/', TodoCreateView.as_view(), name="add-task"),
    path('<pk>/update', TodoUpdateView.as_view(), name="update-task"),
    path('<pk>/delete', TodoDeleteView.as_view(), name="delete-task"),

    path('register/', RegisterView.as_view(),name='register'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
]