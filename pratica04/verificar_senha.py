"""
Crie um programa que verifique se uma senha é forte. 

Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 

O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
"""
while True:

    senha = input("\nDigite a senha (ou 'sair' para encerrar): ")

    # Verificação se o user quer encerrar
    if senha.lower() == "sair":
        print("Programa encerrado.")
        break

    """# Verificar o comprimento da senha
    contador = 0
    for caracter in senha:
        contador += 1
        if contador >= 8 and numero:
            print("Senha forte")
            break"""

    # Verificar o comprimento da senha
    if len(senha) < 8:
        print("Senha fraca. A senha precisa ter pelo menos 8 caracteres.")
        continue

    """# Verificar se existe pelo menos um número
    numero = False
    for caracter in senha:
        if caracter in '0123456789':
            numero = True
            break"""

    # Verificar se existe pelo menos um número
    if not any(caractere.isdigit() for caractere in senha):
        print("Senha fraca. A senha precisa ter pelo menos um número.")
        continue

    # Verificar se existe pelo menos um letra
    if not any(caractere.isalpha() for caractere in senha):
        print("Senha fraca. A senha precisa ter pelo menos uma letra.")
        continue

    # Verificar se existe pelo menos um letra maiúscula
    if not any(caractere.isupper() for caractere in senha):
        print("Senha fraca. A senha precisa ter pelo menos uma letra maiúscula.")
        continue

    # Verificar se existe pelo menos um caracter especial
    simbolos = "!@#$%&"
    if not any (caractere in simbolos for caractere in senha):
        print("Senha fraca. A senha precisa ter pelo menos um caracter especial (Ex. '!@#$%&').")
        continue

    print("Senha forte e válida")
    break    