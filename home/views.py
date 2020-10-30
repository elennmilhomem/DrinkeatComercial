from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home_page(request):
    template = loader.get_template('home/homepage.html') 
    context = {}
    return HttpResponse(template.render(context, request))

def login_page(request):
    template = loader.get_template('home/login.html')
    context = {}
    return HttpResponse(template.render(context, request))