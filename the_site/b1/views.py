from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView, RedirectURLMixin
from django.contrib.auth import login, authenticate
from .models import User
from .forms import *


def index(request):
    return render(request, 'index.html')


# class CustomLogoutView(RedirectURLMixin, LogoutView):
#     def get_success_url(self):
#         return self.request.META.get('home', '/')

def registrationView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user = form.save()
            login(request, new_user)
            return render(request, 'registration/reg_success.html')
    else:
        form = RegistrationForm()
        return render(request, 'registration/registration.html', {'form': form})


def loginSuccessView(request):
    applications = Application.objects.filter(user__username = request.user.username)
    return render(request, 'registration/enter_success.html', {'applications':applications})


# def registrationView(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             # user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = RegistrationForm()
#     return render(request, 'registration/registration.html',{'form':form} )


# class registrationView(CreateView):
#     model = User
#     template_name = 'registration/registration.html'
#     form_class = RegistrationForm
#     success_url = '/login'

def personal_account(request):
    return render(request, 'b1/personal_account.html')


class CreateApplication(CreateView):
    form_class = ApplicationForm
    template_name = 'b1/create_application.html'
    success_url = 'create_application/success'

def createApplSuccess(request):
    return render(request, 'b1/application_created.html')
