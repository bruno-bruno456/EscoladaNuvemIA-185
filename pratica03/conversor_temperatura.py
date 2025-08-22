"""
4- Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura,
a unidade de origem
e a unidade para qual deseja converter.
"""

temperatura = float(input("Digite a temperatura: "))

origem = input("Digite a unidade de origem (Ex. C, F ou K): ").upper()
destino = input("Digite a unidade de destino (Ex. C, F ou K): ").upper()


if origem == destino: # Se a unidade de destino e origem forem iguais, mantém-se o mesmo valor
    resultado = temperatura

elif origem == "C": # Se a origem for Celsius, converte para Fahrenheit ou Kelvin
    if destino == "F": # Celsius para Fahrenheit
        resultado = (temperatura * 9/5) + 32
    else: # Celsius para Kelvin
        resultado = temperatura + 273.15 

elif origem == "F": # Se a origem for Fahrenheit, converter para Celsius ou Kelvin
    if destino == "C": # Fahrenheit para Celsius
        resultado = (temperatura - 32) * 5/9
    else: # Fahrenheit para Kelvin
        resultado = (temperatura - 32) * 5/9 + 273.15

else: # Se a origem for Kelvin, converter para Celsius ou para Fahrenheit
    if destino == "C": # Kelvin para Celsius
        resultado = temperatura - 273.15
    else: # Kelvin para Fahrenheit
        resultado = (temperatura - 273.15) * 9/5 + 32   


print(f"{temperatura} {origem} é igual a {resultado:.2f} {destino}")