from django import forms
from . import models


class BrandForm(forms.ModelForm):

    class Meta:
        model = models.Brand
        fields = ['name', 'description']
        widgets = {  # como se fosse uma personalização
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # quantas linhas vao comecar
        }
        labels = {  # alterar a label, nome
            'name': 'Nome',
            'description': 'Descrição'
        }
