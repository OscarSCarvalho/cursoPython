
'''
Argumentos nomeados e não noemeados em funções Python
Argumentos nomeado te nome com sianl de igual
Argumentos não nomeado recebe apenas o argumeto (valor) 
'''


def soma(x, y, z):  # Definição da função soma com três parâmetros: x, y e z
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z) # Exibe os valores de x, y e z, e a soma deles


soma(1, 2, 3) # Chamada da função soma com três argumentos posicionais
soma(1, y=2, z=5)  # Chamada da função soma com o primeiro argumento posicional e os outros dois como nomeados

print(1, 2, 3, sep='-') # Exibe os números 1, 2 e 3 separados por hífens