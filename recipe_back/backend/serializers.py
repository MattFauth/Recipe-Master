from django.contrib.auth.models import User, Group, Permission
from django.db import transaction
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        models = Permission
        fields = '__all__'

class UsuarioDetalhadoSerializer(serializers.ModelSerializer):
    class GroupSerializer(serializers.ModelSerializer):
        permissions = PermissionSerializer(many=True)

        class Meta:
            model = Group
            fields = ['id', 'name', 'permissions']

    groups = GroupSerializer(many=True)
    user_permissions = PermissionSerializer(many=True)

    class Meta:
        model = User
        fields = ['email', 'groups', 'id', 'is_superuser', 'last_login', 'date_joined', 'user_permissions', 'username']

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id', 'cadastrado_em', 'atualizado_em', 'usuario', 'nome', 'sexo', 'cpf', 'telefone', 'endereco',
                  'estado_uf', 'cidade', 'cep']
        read_only_fields = ['cadastrado_em', 'atualizado_em']

class ReceitaSerializer(serializers.ModelSerializer):
    class TipoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tipo
            fields = ['id', 'nome', 'slug']
    class AutorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Autor
            fields = ['id', 'nome']
            read_only_fields = ['cadastrado_em', 'atualizado_em']
    class Meta:
        model = Receita
        fields = ['nome', 'tipo', 'imagem', 'descricao', 'tempo_preparo', 'porcoes', 'ingredientes', 'autor', 'slug']
        read_only_fields = ['cadastrado_em', 'atualizado_em', 'id']

    class AutorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Autor
            fields = ['id', 'nome']
            read_only_fields = ['cadastrado_em', 'atualizado_em']

    tipo_id = serializers.PrimaryKeyRelatedField(queryset=Tipo.objects.all(), required=True, write_only=True)
    autor_id = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all(), required=True, write_only=True)
    tipo = TipoSerializer(read_only=True)
    autor = AutorSerializer(read_only=True)

    class Meta:
        model = Receita
        fields = ['id','nome','tipo_id','tipo','imagem','descricao','tempo_preparo','porcoes','ingredientes','autor_id','autor']
        read_only_fields = ['cadastrado_em', 'atualizado_em', 'slug']

    def create(self, validated_data):
        validated_data['tipo'] = validated_data.pop('tipo_id')
        validated_data['autor'] = validated_data.pop('autor_id')
        return super().create(validated_data)

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['id', 'nome']
        read_only_fields = ['slug']

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome']
        read_only_fields = ['cadastrado_em', 'atualizado_em']

class IndexSerializer(serializers.ModelSerializer):
    class TipoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tipo
            fields = ['id', 'nome', 'slug']

    class ReceitaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Receita
            fields = ['nome', 'tipo', 'imagem', 'descricao', 'tempo_preparo', 'porcoes', 'ingredientes', 'autor', 'slug']
            read_only_fields = ['cadastrado_em', 'atualizado_em', 'id']