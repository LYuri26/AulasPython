from django.shortcuts import render, redirect
from .forms import PedidoForm, ProdutoForm, CategoriaForm
from .models import Produto, Categoria


def lista_produtos(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    produto_form = ProdutoForm(request.POST or None)
    categoria_form = CategoriaForm(request.POST or None)
    if request.method == 'POST':
        if produto_form.is_valid():
            produto_form.save()
            return redirect('lista_produtos')
    return render(request, 'lista_produtos.html', {'produtos': produtos, 'categorias': categorias, 'produto_form': produto_form, 'categoria_form': categoria_form})


def criar_pedido(request):
    form = PedidoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    return render(request, 'criar_pedido.html', {'form': form})


def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    return redirect('lista_produtos')


def inserir_categoria(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # Substitua pelo nome da view de listagem de produtos
            return redirect('lista_produtos')
    return render(request, 'inserir_categoria.html', {'form': form})
