"""
3- Calculadora de IMC
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso" 
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
 Para os demais cenários: classificacao = "Obeso"
"""
# Variavéis (Entrada)
peso = float(input("Digite seu peso em Kg (Ex. 70.5): "))
altura = float(input("Digite sua altura em metros (Ex. 1.85): "))

# Cálculo do ICM
imc = peso / (altura ** 2)

# Classificação
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"        


#print(f"\nSeu IMC é {imc:.1f}")
#print(f"Classificação: {classificacao}\n")

print(F"""
Seu IMC é {imc:.1f}
Classificação: {classificacao}
""")