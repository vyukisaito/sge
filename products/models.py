from django.db import models
from brands.models import Brand
from categories.models import Category


class Product(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(null=True, blank=True)
    serie_number = models.CharField(max_length=200, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)  # o decimal field é o ideal para preço, vendas
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)  # o decimal field é o ideal para preço, vendas
    quantity = models.IntegerField(default=0)  # qnd cria um produto temos zero no estoque por padrao
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
