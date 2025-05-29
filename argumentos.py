"""
Argumentos nomeados e não nomeados em funçoes Python
Arguentos nomeados tem nome co sinal de igual
Argumentos não nomeados recebe apenas o argumento (valor)
"""

def soma(x, y):  #função soma com dois argumentos x e y
    print (f'{x=} y= {y}')  #soma os dois argumentos e imprime o resultado

soma(y=10, x=20)  #chama a função soma com os argumentos 10 e 20





def soma(x, y, z=0):  # Definindo valores padrão para os argumentos x, y e z
    if z:  # Verifica se z foi fornecido
        print(f'{x=} {y=} {z=}', x + y + z)  # Soma os três argumentos e imprime o resultado
    else:  # Caso z não seja fornecido
        print(f'{x=} {y=}', x + y)  # Soma apenas x e y e imprime o resultado


    soma(1,2)
    soma(3,5)
    soma(100, 200)
    soma(7, 9, 0)


    """
    Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
    """

    def escopo():
        x = 1
        print(x)


    escopo()  # Chama a função escopo, que imprime o valor de x (1)