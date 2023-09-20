from django.contrib import admin
from django.urls import path, include
from appcodecolinas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastrocliente, name='cadastrocliente'),
    path('processarcadastro/', views.processarcadastro, name='processarcadastro'),
    path('', views.index, name='index'), 
]
