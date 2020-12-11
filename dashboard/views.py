from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PostForm, UsuarioForm
from datetime import datetime
from django.views.generic.base import View
from .models import Post, Usuario, Categoria
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, UpdateView


class UsuarioUpdateView(UpdateView, LoginRequiredMixin):
    form_class = UsuarioForm
    template_name = 'dashboard/dashboard_usuario_create.html'
    success_url = '/dash'
    model = Usuario 
    # fields = ['instagram', 'twitter', 'cidade', 'descricao_usuario', 'foto_perfil']

class UsuarioFormView(FormView, LoginRequiredMixin):
    form_class = UsuarioForm
    template_name = 'dashboard/dashboard_usuario_create.html'
    success_url = '/dash'

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            usuario = form.save()
            usuario.user = request.user
            usuario.pontuacao = 0
            usuario.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class FeedView(LoginRequiredMixin, View):
    template_name = 'dashboard/dashboard_feed.html'

    def get(self, request):
        if Usuario.objects.filter(user=self.request.user.id):
            context = {
                'posts': Post.objects.all().order_by('-data'), 
                'usuario': Usuario.objects.filter(user=self.request.user.id)[0],
                'categorias': Categoria.objects.filter(user=self.request.user.id)
            }
            return render(request, 'dashboard/dashboard_feed.html', context=context)
        else:
            print("Não foi")
            return redirect('/dash/register/usuario')


@login_required(login_url='/login')
def register_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(request)
            post.user = User.objects.get(id=request.user.id)
            post.data = datetime.now()
            post.save()
            return redirect('/dash/')
        else:
            print("ERROR")
    else:
        form = PostForm()
    return render(request, 'dashboard/dashboard_feed_post.html', {'form': form})
