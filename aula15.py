"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

def verificar_par_ou_impar():   # primeiro criei função verificar par ou impar
    numero = input("Digite um número inteiro: ")  #dentro da função criei input para digitar numero

    try:  #Python tentará executar esse código. Se não houver erros, o código dentro do bloco try é executado normalmente, e o bloco except é ignorado.
        numero_inteiro = int(numero) 
        if numero_inteiro % 2 == 0: #faz divisão do mumero digitado input, se sobrar e impar, se no caso igual a zero e par
            print(f"O número {numero_inteiro} é par.")
        else:
            print(f"O número {numero_inteiro} é ímpar.")

    except ValueError:  #Se ocorrer um erro dentro do bloco try, o Python "captura" esse erro e pula diretamente para o bloco except.
        print("Isso não é um número inteiro.")

verificar_par_ou_impar()






    

    








