from django import forms
from .models import TodoList

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2', )

class TodoListForm(forms.ModelForm):
    class Meta:
        model =TodoList
        fields = ('task', 'details', 'complete')

        widgets = {
            'task': forms.TextInput(attrs={'class':'form-control'}),
            'details': forms.Textarea(attrs={'class':'form-control'}),
            # 'complete': form.(attrs={'class':'form-control'}),
        }

