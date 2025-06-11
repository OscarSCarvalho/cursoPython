
x,  y, *resto  =  1, 2, 3, 4   # 5, 6, 7, 8, 9, 10  # Atribui os valores 1 e 2 a x e y, e o restante a resto
print(x, y , resto)  # Imprime os valores de x, y e resto


def soma(*args):
    print(args, type(args))


soma(1,2, 3, 4, 5)  # Chama a função soma com múltiplos argumentos 