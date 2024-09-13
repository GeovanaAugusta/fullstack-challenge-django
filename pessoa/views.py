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
        serializer = PessoaDTO(data=request.data)
        if serializer.is_valid():
            pessoa = PessoaService.criar_pessoa(serializer.validated_data)
            return Response(pessoa, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        pessoa = PessoaService.buscar_pessoa(pk)
        if not pessoa:
            return Response({'detail': 'Pessoa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        data = request.data.copy()
        if 'cpf' in data:
            data.pop('cpf')  

        serializer = PessoaDTO(pessoa, data=data, partial=True)
        if serializer.is_valid():
            pessoa_atualizada = PessoaService.atualizar_pessoa(pk, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        sucesso = PessoaService.excluir_pessoa(pk)
        if sucesso:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'Pessoa não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path='peso-ideal-por-cpf')
    def calcular_peso_ideal_por_cpf(self, request):
        cpf = request.query_params.get('cpf')
        
        if not cpf:
            return Response({"detail": "CPF é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        pessoa = PessoaService.buscar_por_cpf(cpf)
        if not pessoa:
            return Response({'detail': 'Pessoa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
            
        altura = pessoa.get('altura')
        sexo = pessoa.get('sexo')

        if altura is None or sexo is None:
            return Response({'detail': 'Dados incompletos para cálculo do peso ideal'}, status=status.HTTP_400_BAD_REQUEST)

        if sexo == 'M':
            peso_ideal = (72.7 * altura) - 58
        elif sexo == 'F':
            peso_ideal = (62.1 * altura) - 44.7
        else:
            return Response({'detail': 'Sexo inválido para cálculo do peso ideal'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'peso_ideal': peso_ideal}, status=status.HTTP_200_OK)
