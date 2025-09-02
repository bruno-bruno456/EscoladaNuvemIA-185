import csv
def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as e:
        print(f"Erro {e} foi encontrado ao ler o arquivo.")


if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo: ").strip()
    ler_csv(nome_arquivo)


