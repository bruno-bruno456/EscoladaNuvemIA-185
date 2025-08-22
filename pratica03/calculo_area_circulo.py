"""
A fórmula para calcular a área de uma circunferência é: área = π × raio2.
Considerando para este problema que π = 3.14159265: 

Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. 

Entrada: A entrada contém um valor de ponto flutuante (dupla precisão)
, no caso, a variável raio.

Saída: Apresente a mensagem "A=" seguido pelo valor da variável area,
conforme exemplo abaixo, com 4 casas após o ponto decimal.
"""
# Definição das variáveis
pi = 3.14159265
raio = float(input('Insira o valor do raio em cm (Ex.: 10.05): '))

# Cálculo da área
area = pi * (raio ** 2)

# Exibição dos resultados
print(f'A= {area:.4f} cm²')