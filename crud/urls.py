from django.urls import path
from django.contrib.auth import views
from . import views
urlpatterns = [

    path('', views.PasswordEmailSender.as_view(), name='password_reset'),

    path('reset/<uidb64>/<token>/',views.InputsChange.as_view(),
         name='password_reset_confirm'),
    
    path('reset/done/',views.SuccessPasswordChangeDone.as_view(),name='password_reset_complete'),

    path('email_enviado/',views.success_email,name='email_enviado')

]
