from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView
from django.contrib.auth import authenticate,login,logout

from .models import *
from .forms import *



class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'pages/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Дополнительная проверка и отладка
        print("Form is valid. Redirecting to success URL.")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        # Дополнительная проверка и отладка
        print("Form is invalid. Returning to registration page.")
        return response



class LoginView(FormView):
    form_class = LoginForm
    template_name = 'pages/login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        
        user = authenticate(username=username,password=password,email=email)
       
        if user is not None:
            if user.is_active:
                login(self.request,user)
                return redirect('index')
            else:
                return HttpResponse('Ваш аккаунт заблокирован')
        else:
            return HttpResponse(' Такого пользователя не существует')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')