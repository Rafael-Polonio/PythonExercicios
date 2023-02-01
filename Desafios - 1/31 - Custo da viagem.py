# Desenvolva um programa que pergunte a distância da viagem em kilometros.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km
# e R$0,45 para viagens mais longas

d = float(input('Distância da viagem em Km: '))
if d<=200:
    print(f'O preço da passagem é {d*0.5}')
else:
    print(f'O preço da passagem é {d*0.45}')