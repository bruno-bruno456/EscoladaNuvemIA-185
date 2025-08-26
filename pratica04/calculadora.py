while True:
    try:    
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, - , *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2    
        else:
            raise ValueError("Operação inválida")
            #resultado = "Operação inválida"

        print(f"Resultado: {resultado}")
        break

    except ZeroDivisionError:
        print("Erro de Divisão por zero não permitida. Por favor, tente novamente.")    
    except ValueError as e:
        print(f"Erro {e}. Por favor, tente novamente.")