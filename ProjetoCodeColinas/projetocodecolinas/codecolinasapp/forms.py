from django import forms
from .models import Pedido, Produto, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome_cliente', 'produto', 'quantidade']
class ProdutoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        label='Categoria Existente'
    )
    nova_categoria = forms.CharField(
        required=False,
        label='Nova Categoria'
    )

    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'categoria']

    def clean(self):
        cleaned_data = super().clean()
        categoria_existente = cleaned_data.get('categoria')
        nova_categoria = cleaned_data.get('nova_categoria')

        if not (categoria_existente or nova_categoria):
            raise forms.ValidationError(
                'Por favor, selecione uma categoria existente ou insira uma nova.'
            )
        return cleaned_data
