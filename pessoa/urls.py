from django.urls import path
from .views import PessoaViewSet

urlpatterns = [
    path('pessoas/', PessoaViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('pessoas/<int:pk>/', PessoaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('pessoas/buscar-por-cpf/', PessoaViewSet.as_view({'get': 'buscar_por_cpf'})),
]
