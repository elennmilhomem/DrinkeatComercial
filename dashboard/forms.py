from django import forms
from .models import Post, Usuario
from datetime import datetime

class PostForm(forms.ModelForm):
    
    comentario = forms.CharField(max_length=240, label="Escreva um comentário")
    imagem = forms.ImageField(label="Imagem:", allow_empty_file=True)

    class Meta: 
        model = Post
        fields = ['comentario', 'imagem',]
    
    # def save(self,request):
    #     # print("oi")
    #     # print(request.FILES['imagem'].name)
    #     post = Post.objects.create(
    #         comentario = self.cleaned_data['comentario'],
    #         imagem = self.cleaned_data['imagem'],
    #         user = request.user,
    #         data = datetime.now()
    #     )
    #     return post

    