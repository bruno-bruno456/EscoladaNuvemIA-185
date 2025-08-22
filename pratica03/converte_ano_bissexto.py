"""
Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.

Um ano é bissexto se for divisível por 4,
exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

ano = int(input("Digite um ano: "))
print("\n Utilizando Estrutura condicional")
if ano % 4 == 0: # Se o ano for divisível por 4, ele pode ser bissexto
    if ano % 100 == 0: # Se for divisível por 100, precisa ser analisado
        if ano % 400 == 0: # Se divisível também por 400, é bissexto
            print(f"{ano} é um ano bissexto.")
        else:
            print(f"{ano} não é ano bissexto.")    
    else:
        print(f"{ano} é um ano bissexto.")    
else:
    print(f"{ano} não é ano bissexto.")                

print("\n Utilizando and, or")
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")    