"""
Calculadora de Comissão

Faça um programa que leia o 
nome de um vendedor, 
o seu salário fixo e o 
total de vendas efetuadas por ele no mês (em dinheiro). 

Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, 


informar o total a receber no final do mês, com duas casas decimais. 

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente. 
Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.
"""

nome_funcinario = input("Insira o nome do vendedor: ")

salario_fixo = float(input("Informe o salário fixo (Ex. 3500.00): "))
total_vendas = float(input("Informe o total em vendas (Ex. 20000.00): "))

percentual_comissao = 0.15


comissao = total_vendas * percentual_comissao


salario_total = salario_fixo + comissao


print(f"Nome do funcionário: {nome_funcinario}")
print(f"Salário Fixo: R$ {salario_fixo:.2f}")
print(f"Total de Vendas R$ {total_vendas:.2f}")
print(f"Comissão: R$ {comissao:.2f}")
print(f"Salário Total: R$ {salario_total:.2f}")