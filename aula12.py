"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # Alinha à direita com 10 espaços
print(f'{variavel: <10}.') # Alinha à esquerda com 10 espaços
print(f'{variavel: ^10}.') # Alinha ao centro com 10 espaços
print(f'{1000.4873648123746:0=+10,.1f}')    # Formatação de float com 10 caracteres, sinal +, preenchido com zeros, e uma casa decimal
print(f'O hexadecimal de 1500 é {1500:08X}') # Formatação de hexadecimal com 8 caracteres, preenchido com zeros
print(f'{variavel!r}') # Representação da variável com !r 