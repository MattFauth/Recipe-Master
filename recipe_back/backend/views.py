from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
import random

from .serializers import *
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    ordering_fields = ['id', 'username', 'email']
    search_fields = ['username', 'email']
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class UsuarioLogadoDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioDetalhadoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.get(pk=self.request.user.pk)

    def list(self, request, *args, **kwargs):
        usuario = self.get_queryset()
        return Response(self.get_serializer(usuario).data)


class PerfilLogadoViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite obter e cadastrar um perfil para o usuário logado
    """
    serializer_class = PerfilSerializer

    def get_queryset(self):
        return Perfil.objects.filter(usuario=self.request.user)

    def list(self, request, *args, **kwargs):
        perfil = self.get_queryset()
        if perfil.exists():
            serializer = self.get_serializer(perfil.first())
            return Response(serializer.data)

        return Response(None, status=404)


class PerfilViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite recuperar e editar informações sobre perfis de usuários
    """
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()
    filterset_fields = [
        'usuario',
        'estado_uf',
        'cidade',
    ]
    search_fields = [
        'usuario__username',
        'usuario__email',
        'nome',
        'cpf',
        'telefone',
        'endereco',
        'estado_uf',
        'cidade',
        'cep',
    ]
    permission_classes = [permissions.IsAuthenticated]

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()
    filterset_fields = ['usuario', 'estado_uf', 'cidade']
    search_fields = ['usuario__username', 'usuario__email', 'nome', 'cpf', 'telefone', 'endereco', 'estado_uf','cidade', 'cep']
    permission_classes = [permissions.IsAuthenticated]

class TipoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoSerializer
    queryset = Tipo.objects.all().order_by('nome')
    search_fields = ['tipo__nome']
    filterset_fields = ['tipo']

class ReceitaViewSet(viewsets.ModelViewSet):
    serializer_class = ReceitaSerializer
    queryset = Receita.objects.all().order_by('nome')
    filterset_fields = ['autor']
    search_fields = ['autor__perfil__nome', 'tipo__nome', 'tempo_preparo', 'porcoes']
    permission_classes = [permissions.IsAuthenticated]

class AutorViewSet(viewsets.ModelViewSet):
    serializer_class = AutorSerializer
    queryset = Autor.objects.all().order_by('perfil__nome')
    search_fields = ['perfil__nome']