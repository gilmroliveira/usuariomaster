from django.contrib import admin
from django.urls import path
from core.views import listar_produtos, criar_produto, buscar_produto, editar_produto, deletar_produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_produtos, name='listar_produtos'),
    path('criar/', criar_produto, name='criar_produto'),
    path('buscar/', buscar_produto, name='buscar_produto'),
    path('editar/<int:pk>/', editar_produto, name='editar_produto'),
    path('deletar/<int:pk>/', deletar_produto, name='deletar_produto'),
]
