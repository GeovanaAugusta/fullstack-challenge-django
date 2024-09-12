from rest_framework import serializers
from .models import Pessoa

class PessoaDTO(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'data_nasc', 'cpf', 'sexo', 'altura', 'peso']
        
    def validate_nome(self, value):
        if not value.strip():
            raise serializers.ValidationError("O nome não pode estar vazio.")
        return value

    def validate_cpf(self, value):
        if len(value) != 11:
            raise serializers.ValidationError("O CPF deve conter exatamente 11 dígitos.")
        return value

    def validate_sexo(self, value):
        if value not in ['M', 'F']:
            raise serializers.ValidationError("O sexo deve ser 'M' para Masculino ou 'F' para Feminino.")
        return value

    def validate_altura(self, value):
        if value <= 0:
            raise serializers.ValidationError("A altura deve ser um número positivo.")
        return value

    def validate_peso(self, value):
        if value <= 0:
            raise serializers.ValidationError("O peso deve ser um número positivo.")
        return value
