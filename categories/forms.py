from django import forms
from . import models


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = ['name', 'description']
        widgets = {  # como se fosse uma personalização
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # quantas linhas vao comecar
        }
        labels = {  # alterar a label, nome
            'name': 'Nome',
            'description': 'Descrição'
        }
