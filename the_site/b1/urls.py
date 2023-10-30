from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', registrationView, name='registration'),
    # path('registration/', registrationView.as_view(), name='registration'),
    path('appl_processing/', applicationProcessingList, name='apllication_processing'),
    path('appl_processing_list/processing/<int:int_pk>', ApplicationProcessingView.as_view(), name='processing'),

    path('accounts/profile/', loginSuccessView, name='loginSuccess'),
    path('create_application', CreateApplication.as_view(), name='createApplication'),
    path('create_application/success', createApplSuccess, name='createApplSuccess'),
    path('accounts/profile/delete-application/<int:del_pk>', deleteApplicationView, name='deleteApplication')

]