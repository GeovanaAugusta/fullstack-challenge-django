from rest_framework import status, viewsets
from rest_framework.response import Response
from .services import PessoaService
from .serializers import PessoaDTO
from rest_framework.decorators import action 

class PessoaViewSet(viewsets.ViewSet):
    def list(self, request):
        pessoas = PessoaService.listar_pessoas()
        return Response(pessoas, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='buscar-por-cpf')
    def buscar_por_cpf(self, request):
        cpf = request.query_params.get('cpf')
        if not cpf:
            return Response({"detail": "CPF é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        pessoa = PessoaService.buscar_por_cpf(cpf)
        if pessoa:
            return Response(pessoa, status=status.HTTP_200_OK)
        return Response({'detail': 'Pessoa não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        pessoa = PessoaService.buscar_pessoa(pk)
        if pessoa:
            return Response(pessoa, status=status.HTTP_200_OK)
        return Response({'detail': 'Pessoa não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        # O serializer PessoaDTO irá validar os dados enviados na requisição
        serializer = PessoaDTO(data=request.data)
        if serializer.is_valid():
            pessoa = PessoaService.criar_pessoa(serializer.validated_data)
            return Response(pessoa, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = PessoaDTO(data=request.data)
        if serializer.is_valid():
            pessoa = PessoaService.atualizar_pessoa(pk, serializer.validated_data)
            if pessoa:
                return Response(pessoa, status=status.HTTP_200_OK)
            return Response({'detail': 'Pessoa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        sucesso = PessoaService.excluir_pessoa(pk)
        if sucesso:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'Pessoa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
