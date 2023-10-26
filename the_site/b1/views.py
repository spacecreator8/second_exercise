from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView, RedirectURLMixin
from django.contrib.auth import login, authenticate
from .models import User
from .forms import RegistrationForm



def index(request):
    return render(request, 'index.html')

# class CustomLogoutView(RedirectURLMixin, LogoutView):
#     def get_success_url(self):
#         return self.request.META.get('home', '/')

def registrationView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html',{'form':form} )




# class registrationView(CreateView):
#     model = User
#     template_name = 'registration/registration.html'
#     form_class = RegistrationForm
#     success_url = '/login'

def personal_account(request):
    return render(request, 'b1/personal_account.html')