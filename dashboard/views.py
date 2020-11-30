from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def dashboard_index(request):
    template = loader.get_template('dashboard/dashboard_index.html')
    context = {}
    return HttpResponse(template.render(context, request))