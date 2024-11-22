from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # ao criar, vai ser colocado a data automaticamente
    updated_at = models.DateTimeField(auto_now=True)  # vai criar a data, mas pode ser alterada caso o produto seja editado

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
