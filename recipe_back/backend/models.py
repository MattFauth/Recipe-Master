from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Perfil(models.Model):
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    usuario = models.OneToOneField(User, models.CASCADE)
    nome = models.CharField(max_length=128, db_index=True)
    sexo = models.CharField(max_length=1, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True, unique=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.TextField(max_length=512, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    estado_uf = models.CharField(max_length=2, null=True, blank=True)
    cidade = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.nome)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.perfil.nome


class Receita(models.Model):
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    nome = models.TextField(max_length=128, db_index=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True)
    imagem = models.ImageField(null=True, blank=True)
    descricao = models.TextField(max_length=1024, null=True, blank=True)
    tempo_preparo = models.CharField(max_length=3)
    porcoes = models.CharField(max_length=2)
    ingredientes = models.TextField(max_length=1024, null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=128)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.nome)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.nome
