"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('dobrar o nemero que foi digitado: ')


try:  #tenar verificar codigo correto
    numero_float = float(numero_str)  #string no input acima  convertida ára numero flutiante
    print('FLOAT:', numero_float) 
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:  #se caso estiver com erro pula oara exeção(aviso do erro)
    print('Isso não é um número')

