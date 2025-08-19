"""
4- Calculadora de Preço Total

Desenvolva um programa que calcule o preço total de uma compra. 
Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 

O programa deve calcular o preço total e exibir todas as informações,
incluindo o resultado final.
"""
# Declaração de variáveis
nome_produto = "Cadeira Infantil" # String
preco_unitario = 12.40 # Float
quantidade = 3 # Inteiro

# Cálculo do Valor total
preco_total = preco_unitario * quantidade

# Print como resultado final

print(f"Produto: {nome_produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço total: R$ {preco_total:.2f}")