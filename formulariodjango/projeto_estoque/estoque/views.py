from django.shortcuts import render, get_object_or_404, redirect
from .models import ItemEstoque
from .forms import ItemForm

def lista_estoque(request):
    itens = ItemEstoque.objects.all()
    return render(request, 'estoque/lista_estoque.html', {'itens': itens})

def adicionar_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estoque')
    else:
        form = ItemForm()
    return render(request, 'estoque/adicionar_item.html', {'form': form})

def editar_item(request, id):
    item = get_object_or_404(ItemEstoque, pk=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('detalhes_item', id=id)
    else:
        form = ItemForm(instance=item)
    return render(request, 'estoque/editar_item.html', {'form': form})
