from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', registrationView, name='registration'),
    # path('registration/', registrationView.as_view(), name='registration'),
    path('pers_acc/', personal_account, name='personal_account'),

]