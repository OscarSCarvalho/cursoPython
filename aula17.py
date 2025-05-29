"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('digite seu nome: ')
tamanho_nome = len(nome)   #len(nome): A função len() retorna o número de caracteres na string nome.
 
if tamanho_nome >=1:
    if tamanho_nome  <= 4:  # si
        print('seu nome é curto')

    elif tamanho_nome >= 5 and tamanho_nome <=6 :  #senao si 
        print('seu nome é normal')

    else:
        print('seu nome é muito grande') #se não






        







