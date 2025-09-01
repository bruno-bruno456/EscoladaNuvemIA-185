"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""
import datetime # importação o módulo datetime, permite trabalhar com datas no Python

# Definindo uma função que vai receber o ano de nascimento
def calcular_idade_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

# Entrada de dados
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula a idade em dias, chamando a função
idade_dias = calcular_idade_dias(ano_nascimento)

# Saída dos dados, exibição do resultado
print(f"Sua idade aproximada em dias é {idade_dias} dias")
