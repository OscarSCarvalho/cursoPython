'''def print():
    print('Varrias1')
    print('Varrias2')
    print('Varrias3')
    print('Varrias4')
    
'''

'''def imprimir(a, b, c):
    print(a, b, c)
    

imprimir(1, 2, 3)

'''
'''def saudacao(nome='sem nome'): # Define a função saudacao com um parâmetro nome, que tem um valor padrão 'sem nome'caso eu não asse nenhnhum valor na funçao votara sem nome 
    print(f'Olá, {nome}! Seja bem-vindo(a)!') # Exibe uma saudação personalizada


saudacao('Oscar') # Chamadas da função saudaccao com diferentes nomes
saudacao('Maria')
saudacao('João')
saudacao()
saudacao('Ana') # Chamada da função saudacao com o nome 'Ana'  '''

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)