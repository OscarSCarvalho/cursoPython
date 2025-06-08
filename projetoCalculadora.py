'''
  Projeto: Calculadora de 4 operações com tratamento de erros
🔹 Funcionalidades:
Soma

Subtração

Multiplicação

Divisão

Sair
 
------------------------------------------------------------------------------------
O que estamos aplicando aqui:
try para proteger a entrada e os cálculos

except ValueError para entrada não numérica

except ZeroDivisionError para evitar a divisão por zero

except Exception como segurança extra (opcional)

finally para mostrar sempre que a operação terminou

 '''




def menu():
    print("\n=== CALCULADORA SIMPLES ===") # Exibe o título do menu
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")


while True: # Loop infinito para manter o programa rodando até o usuário escolher sair
    menu()
    escolha = input("Escolha uma opção (1 a 5): ")

    if escolha == "5":
        print("Encerrando o programa. Até logo!")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == "1":
            print(f"Resultado: {num1 + num2}")
        elif escolha == "2":
            print(f"Resultado: {num1 - num2}")
        elif escolha == "3":
            print(f"Resultado: {num1 * num2}")
        elif escolha == "4":
            print(f"Resultado: {num1 / num2}")
        else:
            print("Opção inválida. Escolha de 1 a 5.")

    except ValueError:
        print("Erro: Você digitou um valor que não é número.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

    finally:
        print("Operação finalizada.\n")
