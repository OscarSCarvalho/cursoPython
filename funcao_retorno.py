'''retorno de valores de uma função (return)
'''


def soma(x, y):
    print('olha a função soma')
    print('comofunciona')
    print('com return')
    print('no final')
    return x + y  # A função soma recebe dois argumentos x e y e retorna a soma deles


soma1 = soma(2, 2)  # Chamada da função soma com os argumentos 1 e 2, e o resultado é armazenado em soma1
soma2 = soma(3, 3)  # Chamada da função soma com os argumentos 3 e 4, e o resultado é armazenado em soma2

print(soma1 + soma2)