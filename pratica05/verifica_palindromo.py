"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). 

Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""


"""
Palindromo é aquilo que escrevemos de trás para frente da mesma forma que escrevemos naturalmente.
Ex:
arara
Ana
A cara rajada da jararaca
"""

def palindromo(frase):
    # Remover os espaços e convertendo para minúsculo
    texto_limpo = ''.join(char.lower()
                          for char in frase
                          if char.isalnum()
                          )
    return texto_limpo == texto_limpo[::-1] # comparando o texto limpo a sua versão invertida

texto = input("Digite a expressão ou palavra: ")
resultado = palindromo(texto)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"'{texto}' é um palindromo? {resposta}") 