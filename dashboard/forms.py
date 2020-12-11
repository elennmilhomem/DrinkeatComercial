from django import forms
from .models import Post, Usuario
from datetime import datetime

class PostForm(forms.ModelForm):
    
    comentario = forms.CharField(max_length=240, label="Escreva um comentário:")
    imagem = forms.ImageField(label="Imagem:", allow_empty_file=True)

    class Meta: 
        model = Post
        fields = ['comentario', 'imagem',]
    
class UsuarioForm(forms.ModelForm):

    instagram = forms.CharField(max_length=30, label="Instagram:")
    twitter = forms.CharField(max_length=30, label="Twitter:")
    cidade = forms.CharField(max_length=30, label="Cidade:")
    descricao_usuario = forms.CharField(max_length=120, label="Sobre mim:")
    foto_perfil = forms.ImageField(label="Foto de usuário")
    
    class Meta:
        model = Usuario
        fields = ['instagram', 'twitter', 'cidade', 'descricao_usuario', 'foto_perfil']