from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from backend import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register('perfil-logado', views.PerfilLogadoViewSet, basename='perfil-logado')
router.register('usuario-logado', views.UsuarioLogadoDetailsViewSet, basename='usuario-logado')
router.register('perfis', views.PerfilViewSet, basename='perfis')
router.register('receitas', views.ReceitaViewSet)
router.register('autores', views.AutorViewSet)
router.register('index', views.IndexViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/token-auth/', obtain_jwt_token),
    path(r'api/token-refresh/', refresh_jwt_token),
]