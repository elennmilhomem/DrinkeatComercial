from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View



# Create your views here.
def home_page(request):
    template = loader.get_template('home/homepage.html') 
    context = {}
    return HttpResponse(template.render(context, request))

def login_page(request):
    template = loader.get_template('home/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def cadastro_page(request):
    template = loader.get_template('home/cadastro.html')
    context = {}
    return HttpResponse(template.render(context, request))

def logout_user(request):
    logout(request)
    return redirect('home/')

class AutenticacaoView(View):

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dash')
        else:
            return render(request,'home/login.html',{"erro": "Usuário não encontrado. Por favor, verifique login e senha."})
