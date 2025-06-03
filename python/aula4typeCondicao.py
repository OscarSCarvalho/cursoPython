# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadbres para "questionar".
# Dentre eles o == , que é um operador lógico que
# questiona se um valor é igual a outro


nome = "Oscar"
altura = 1.80
idade = 17



print(type(10==10)) # compara se informaçao verdadeira ou falsa no caso essa iprime na tela True(verdadiero)
print(10==11)  # essa ira imprimi False(falsa)
print(type(True))  #tipo de dado 
print(type(False))  #boleano
print(type("Oscar"))  #sttring
print(type(1.3)) #float 

print(type(nome), type(altura), type(idade))  # imprime o tipo de dado de cada variavel

if nome== 'Oscar' and altura == 1.80 and idade >= 18: #condição que verifica se o nome é Oscar, a altura é 1.80 e a idade é maior ou igual a 18
    print("Tudo certo, Oscar!")
else:
    print("Sua idade não esta dentro  das regras , Oscar!")


