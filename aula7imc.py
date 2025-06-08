#calculo immc

nome = 'Oscar Carvalho'
peso = 105
altura = 1.80
imc = peso / (altura ** 2)  # >>> peso divido pela altura elevada ao quadrado(**) 

if  imc >32:
    print('Nome: ', nome , ', Aatura: ',altura)
    print('seu peso e: ', peso)
    print(f"Seu IMC é: {imc:.2f}")  # formatando varieval imc e duas casas decimais 

    print('seu nivel de obesidade nivel II')
else:
    print('esta na media do peso ')
