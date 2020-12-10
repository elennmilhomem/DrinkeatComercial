from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from datetime import datetime
from django.views.generic import TemplateView
from .models import Post, Usuario, Categoria

class FeedView(TemplateView):
    template_name = 'dashboard/dashboard_feed.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(*args,**kwargs)
        context['posts'] = Post.objects.all()
        context['usuario'] = Usuario.objects.filter(user=self.request.user.id)[0]
        context['categorias'] = Categoria.objects.filter(user=self.request.user.id)
        return context



@login_required(login_url='/login')
def dashboard_index(request):
    template = loader.get_template('index_base_dashboard.html')
    context = {}
    return HttpResponse(template.render(context, request))

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