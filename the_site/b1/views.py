import uuid

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, RedirectURLMixin
from django.contrib.auth import login, authenticate
from .models import User
from .forms import *
from django.shortcuts import get_object_or_404


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
    applications = Application.objects.filter(username=request.user.username)
    return render(request, 'registration/enter_success.html', {'applications': applications})


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




class CreateApplication(CreateView):
    form_class = ApplicationForm
    template_name = 'b1/create_application.html'
    success_url = 'create_application/success'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


def createApplSuccess(request):
    return render(request, 'b1/application_created.html')


# def deleteApplicationView(request, del_pk):
#     object = Application.objects.get(pk=del_pk)
#     object.delete()
#     return redirect('loginSuccess')

def deleteApplicationView(request, del_pk):
    object = Application.objects.get(pk=del_pk)
    if request.method == 'POST':
        form = DoYouWantDel(request.POST)
        if form.is_valid():
            if (form.cleaned_data.get('sure') == 'yes'):
                object.delete()
                return redirect('loginSuccess')
            else:
                return redirect('loginSuccess')
    else:
        form = DoYouWantDel()
        return render(request, 'b1/are_you_sure.html', {'form': form, 'object':object})


class ApplicationProcessingList(ListView):
    model = Application
    queryset = Application.objects.order_by('-date_creation')
    context_object_name = 'list'
    template_name = 'b1/list_applications.html'
    paginate_by = 10


class ApplicationProcessingView(UpdateView):
    model = Application
    form_class = ApplProcessingForm
    success_url = '/appl_processing/'
    template_name = 'b1/processing.html'

    def get_object(self):
        post_id = self.kwargs.get('int_pk')
        obj = get_object_or_404(Application, id=post_id)
        return obj











