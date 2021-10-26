from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from validate_docbr import CPF


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'CPF:',}

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError('Este e-mail {} já cadastrado!'.format(e))

        return e

    # def valida_cpf(self):
    #     cpf = CPF()  # instancia
    #     username = self.cleaned_data['username']
    #
    #     if cpf.validate(username) == False:
    #         raise ValidationError('Este CPF {} é invalido!'.format(username))
    #
    #     return username




