from django.db import models

class Categoria(models.Model):
    nome_item = models.CharField(max_length=180, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_item

class Categoria(models.Model):
    nome = models.CharField(max_length=180, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    preco = models.DecimalField(null=False, blank=False)

    disponivel = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)  
    atualizado_em = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.nome