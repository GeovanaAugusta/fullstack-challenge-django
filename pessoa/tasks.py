from .models import Pessoa

class PessoaTask:
    
    @staticmethod
    def buscar_por_cpf(cpf):
        try:
            return Pessoa.objects.get(cpf=cpf)
        except Pessoa.DoesNotExist:
            return None
    
    @staticmethod
    def listar_todos():
        return Pessoa.objects.all()

    @staticmethod
    def buscar_por_id(pessoa_id):
        try:
            return Pessoa.objects.get(id=pessoa_id)
        except Pessoa.DoesNotExist:
            return None

    @staticmethod
    def criar_pessoa(dados):
        pessoa = Pessoa.objects.create(**dados)
        return pessoa

    @staticmethod
    def atualizar_pessoa(pessoa_id, dados):
        pessoa = PessoaTask.buscar_por_id(pessoa_id)
        if pessoa:
            for key, value in dados.items():
                setattr(pessoa, key, value)
            pessoa.save()
            return pessoa
        return None

    @staticmethod
    def excluir_pessoa(pessoa_id):
        pessoa = PessoaTask.buscar_por_id(pessoa_id)
        if pessoa:
            pessoa.delete()
            return True
        return False
