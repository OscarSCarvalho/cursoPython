
"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61
km_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RANGE = 1


if velocidade > RADAR_1:
    print('velocidade acima radar 1')

if km_carro >= (LOCAL_1 + RANGE)and\
      velocidade >= RADAR_1:
    print('Multa')
