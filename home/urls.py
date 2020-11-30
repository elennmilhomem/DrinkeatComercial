from django.urls import path
from . import views


urlpatterns = [  
    path('', views.home_page, name = 'home_page'),
    path('login/',views.login_page, name = 'login_page'),
    path('cadastro/',views.cadastro_page, name = 'cadastro'),
    path('logar/',views.AutenticacaoView.as_view(), name = 'logar_user'),
    path('deslogar/',views.logout_user, name='deslogar_user')
]   
