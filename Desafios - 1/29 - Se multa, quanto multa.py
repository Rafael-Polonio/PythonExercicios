#escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa custará R$7,00 para cada km/h acima do limite.

v = float(input('Velocidade do carro em km/h: '))
if v > 80:
    m = (v-80)*7
    print(f'Você ultrapassou o limite de velocidade, otário'
          f'Sua multa será de {m}')