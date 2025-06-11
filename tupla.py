
# Tupla com vários elementos
minha_tupla = (1, 2, 3, 4)

# Tupla com um único elemento (tem que ter a vírgula)
tupla_unica = (5,)

# Tupla sem parênteses (Python entende automaticamente)
outra_tupla = 10, 20, 30


print (type(minha_tupla))  # Exibe a tupla com vários elementos
print(type(tupla_unica))  # Exibe a tupla com um único elemento  
print(outra_tupla)  # Exibe a tupla sem parênteses  

print(minha_tupla[0])  # Acessa o primeiro elemento da tupla com vários elementos 

a, b =(10, 20) # Atribuição de múltiplos valores a variáveis a partir de uma tupla
print(a) #  Exibe o valor de a
print(b) # Exibe o valor de b 

#usasno ttuplaaoinves de listas 
dias_da_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')  # Tupla com os dias da semana
print(dias_da_semana[0])

#tuplaspodemser chaves em dicionarios
localizacoes ={
    (10.0, 20,0): 'loja A',
    (30.0, 40.0): 'loja B', 
}
print(localizacoes)  # Acessa o valor associado à chave (10.0, 20.0) no dicionário localizacoes

#Tuplas Para desempacotar valores fixos

pessoa = ('João', 30, 'Analista') #variável pessoa é uma tupla com três elementos: nome, idade e cargo

nome, idade, cargo = pessoa  # Desempacota os valores da tupla pessoa em variáveis nome, idade e cargo
print(nome)  # João
print(idade) # 30
print(cargo) # Analista
