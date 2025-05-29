'''programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

entrada = input('Digite a hora em numeros inteiros ')  #criei variavel entrada e coloqeui um input para digitar 
                                                       #oque representa essa variavel
try:
    hora = int(entrada) # nessa variavl atribui variavel entrada ja convertida para int

    if hora >= 0 and hora <= 11:  # aqui começo a compraraçoes com input entrada
        print('Bom dia')

    elif hora >= 12 and hora <= 17:
        print('Boa tarde')    
    elif hora >= 18 and hora <= 23:
        print('Boa noite')  
    else:
        print('Hora invalida')    
except:
    print('Por favor digite apenas numeros inteiros')


    #usei try -  except para verificaçoes das entradas 
    # try verifica codigo esta dentro do correto
    # se nao estiver dentro do correto é e xecutado o except