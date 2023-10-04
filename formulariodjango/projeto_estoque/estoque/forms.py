from django import forms
from .models import ItemEstoque

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemEstoque
        fields = ['nome', 'descricao', 'quantidade_disponivel']
