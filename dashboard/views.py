from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from datetime import datetime


@login_required(login_url='/login')
def dashboard_index(request):
    template = loader.get_template('dashboard/dashboard_feed.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login')
def post_post(request):
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
    return render(request, 'dashboard/dashboard_feed.html', {'form': form})