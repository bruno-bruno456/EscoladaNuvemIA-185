"""
Crie um programa que permita a um professor registrar as notas de uma turma. 

O programa deve continuar solicitando notas até que o professor digite 'fim'. 

Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. 

No final, deve exibir a média da turma.
"""
# notas = []
soma = 0
quantidade = 0
while True:
    try:
        entrada = input("Digite a nota do aluno ou digite 'fim' para encerrar: ")
        if entrada.lower() == "fim":
            break
        nota = float(entrada)
        # if nota >= 0 and nota <= 10: # forma tradicional
        if 0 <= nota <= 10: # forma encadeada
            soma += nota # soma = soma + nota
            quantidade += 1  # quantidade = quantidade + 1  
            #notas.append(nota)
        else:
            print("Nota inválida. Digite um valor de 0 a 10.")    
            continue
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim' para encerrar.")

if quantidade > 0:
    media = soma / quantidade
    # media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f}")
    print(f"Total de notas válidas: {quantidade}")
    # print(f"Total de notas válidas: {len(notas)}")
else:
    print("Nenhuma nota válida foi registrada.")    
        