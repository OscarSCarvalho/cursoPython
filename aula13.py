"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

Ele tenta transformar o que você digitou em um número com vírgula (chamado de "número flutuante", tipo 3.5), e depois mostra o dobro desse número.

 try:
Esse comando diz:
👉 "Tente fazer isso aqui embaixo. Se der errado, não pare tudo, apenas avise que deu erro."

numero_float = float(numero_str)
👉 Aqui, o computador tenta pegar um texto (por exemplo "5.5") e transformar isso em um número de verdade (5.5).

⚠️ Mas se você escrever algo como "banana" em vez de um número, vai dar erro.

print('FLOAT:', numero_float)
👉 Ele mostra o número que foi convertido.
Exemplo:
Se você digitou "8.3", ele vai mostrar:

print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
👉 Aqui ele faz a conta do dobro do número e mostra isso com duas casas decimais (ex: 16.60).

Se você digitou "8.3", ele mostra:

except:
👉 Se o que você digitou não for um número, o computador pula tudo que está dentro do "try" e vem aqui para dar um aviso.

 print('Isso não é um número')
👉 Ele mostra essa mensagem se você digitou algo errado, como "maçã" ou "abc":

"""

numero_str = input('dobrar o nemero que foi digitado: ')


try:  #tenar verificar codigo correto
    numero_float = float(numero_str)  #string no input acima  convertida ára numero flutiante
    print('FLOAT:', numero_float) 
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:  #se caso estiver com erro pula oara exeção(aviso do erro)
    print('Isso não é um número')

