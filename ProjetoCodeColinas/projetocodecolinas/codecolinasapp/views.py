from django.shortcuts import render
from .models import Produto
from .forms import PedidoForm
from django.shortcuts import render, redirect
from django.contrib import messages

def lista_produtos(request):
    categoria = request.GET.get('categoria')
    produtos = Produto.objects.all()

    if categoria:
        produtos = produtos.filter(categoria=categoria)

    if not produtos:
        messages.error(request, 'Categoria inválida.')

    return render(request, 'lista_produtos.html', {'produtos': produtos})


def criar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecione para a página de lista de produtos
            return redirect('lista_produtos')
    else:
        form = PedidoForm()

    return render(request, 'criar_pedido.html', {'form': form})

