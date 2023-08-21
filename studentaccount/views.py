from django.shortcuts import render
from django.views import generic
from django import views
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.

class LoginView(generic.View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')

        return render(request, 'login.html', {'form': form})
    

class LogoutView(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')