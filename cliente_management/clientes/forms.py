from django import forms
from .models import Cliente

from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'endereco', 'data_de_nascimento', 'cpf', 'sexo']
        widgets = {
            'data_de_nascimento': forms.DateInput(attrs={'type': 'date'}, format='%d/%m/%Y'),
        }

