from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from .forms import PostForm

# Create your views here.
@login_required(login_url='/login')
def dashboard_index(request):
    template = loader.get_template('dashboard/dashboard_feed.html')
    context = {}
    return HttpResponse(template.render(context, request))

class FeedView(FormView):
    form_class = PostForm 
    template_name = 'dashboard/dashboard_feed.html'
    success_url = '/dash'

    # def post(self,request):
    #     form_class = self.get_form_class()
    #     post_form = self.get_form(form_class)
    #     if post_form.is_valid():
    #         # post = post_form.save(request)
    #         print("post foi")
    #         return self.form_valid(post_form)
    #     else:
    #         return self.form_invalid(post_form)

    def form_valid(self, form):
        post = form.save()
        post.save()
        return redirect('/dash')
