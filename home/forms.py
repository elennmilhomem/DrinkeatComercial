from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UsuarioForm(forms.Form):
    username = forms.CharField(
        label="Nome Usuário",
        widget=forms.TextInput(
            # attrs={'placeholder': 'Maria ..'}
        ),
    )

    email = forms.EmailField(
        label="E-mail",
    )

    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)

    password2 = forms.CharField(label="Confirmar Senha", widget=forms.PasswordInput)
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("A senhas não correspondem")
        return password2

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user