from django.http import HttpResponse, Http404
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . forms import Custom

# https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.views.PasswordResetView
class PasswordEmailSender(auth_views.PasswordResetView):
    # Exibe um campo para o usuário digitar o email. usuário deve ser is_active.
    form_class = Custom
    template_name='email_form.html'
    success_url = reverse_lazy("email_enviado")

class SuccessPasswordChangeDone(auth_views.PasswordResetCompleteView):
    # Apresenta uma visualização que informa ao usuário que a senha foi alterada com sucesso.
    template_name = "success_template_password.html"

#https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.views.PasswordResetView
class InputsChange(auth_views.PasswordResetConfirmView):
    template_name = "new_password.html"


def success_email(request):
    if not request.POST:
        return HttpResponse('Email enviado com sucesso')
    else:
        return Http404('Erro')

# O email não será enviado caso não exista na base de dados.