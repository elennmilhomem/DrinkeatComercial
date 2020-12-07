from django import forms
from .models import Post, Usuario
from datetime import datetime

class PostForm(forms.Form):
    comentario = forms.CharField(max_length=240, label="Escreva um comentário")
    imagem = forms.FileField(label="Adicionar uma imagem", widget=forms.ClearableFileInput())

    class Meta: 
        model = Post
        fields = ['comentario', 'imagem']
    
    # def save(self,request):
    #     print("oi")
    #     print(request.FILES['imagem'])
    #     post = Post.objects.create(
    #         comentario = self.cleaned_data['comentario'],
    #         imagem = self.cleaned_data['imagem'],
    #         usuario = Usuario.objects.get(user = request.user.id),
    #         data = datetime.now()
    #     )
    #     return post

    