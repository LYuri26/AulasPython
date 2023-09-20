from django.shortcuts import render, redirect
from .models import Cliente

def cadastrocliente(request):
    return render(request, 'cadastrocliente.html')

def processarcadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        empresa = request.POST.get('empresa')
        setor = request.POST.get('setor')
        mensagem = request.POST.get('mensagem')

        # Salvar no banco de dados
        Cliente.objects.create(nome=nome, email=email, telefone=telefone, empresa=empresa, setor=setor, mensagem=mensagem)

        return redirect('confirmacao_cadastro')

    return render(request, 'cadastrocliente.html')

def index(request):
    return render(request,'index.html')

def confirmacao_cadastro(request):
    return render(request, 'confirmacaocadastro.html')
