from .tasks import PessoaTask
from .serializers import PessoaDTO

class PessoaService:
    
    @staticmethod
    def buscar_por_cpf(cpf):
        pessoa = PessoaTask.buscar_por_cpf(cpf)
        if pessoa:
            return PessoaDTO(pessoa).data
        return None
    
    @staticmethod
    def listar_pessoas():
        pessoas = PessoaTask.listar_todos()
        return PessoaDTO(pessoas, many=True).data

    @staticmethod
    def buscar_pessoa(pessoa_id):
        pessoa = PessoaTask.buscar_por_id(pessoa_id)
        if pessoa:
            return PessoaDTO(pessoa).data
        return None

    @staticmethod
    def criar_pessoa(dados):
        pessoa = PessoaTask.criar_pessoa(dados)
        return PessoaDTO(pessoa).data

    @staticmethod
    def atualizar_pessoa(pessoa_id, dados):
        pessoa = PessoaTask.atualizar_pessoa(pessoa_id, dados)
        if pessoa:
            return PessoaDTO(pessoa).data
        return None

    @staticmethod
    def excluir_pessoa(pessoa_id):
        return PessoaTask.excluir_pessoa(pessoa_id)
