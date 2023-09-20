from django.shortcuts import render, redirect

def cadastrocliente(request):
    return render(request, 'cadastrocliente.html')

def processarcadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        # ... outros campos ...
        mensagem = request.POST.get('mensagem')
        # Faça o que for necessário com os dados

        # Por exemplo, você pode salvar os dados em um banco de dados:
        # Cliente.objects.create(nome=nome, email=email, ...)

        # E então redirecionar para uma página de confirmação ou outra página
        return render(request, 'confirmacaocadastro.html')

def index(request):
    return render(request,'index.html')