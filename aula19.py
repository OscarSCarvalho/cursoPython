'''Repetições
while (enquanto)
Executa uma ação enquanto uma condição for vedadeira 
Loop infinito -> quando um codigo não tem fim
'''


condicao = True

while condicao:
    nome = input('Digite um nome: ')
    print(f'o nome : {nome}')

    if nome == 'sair':
        break
    print('acabou')
