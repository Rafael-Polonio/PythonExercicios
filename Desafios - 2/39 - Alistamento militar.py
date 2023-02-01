# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# se ele ainda vai se alistar ao serviço militar;
# se é hora de se alistar;
# se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import time

nasc = int(input('Informe seu ano de nascimento: '))

import datetime
hoje = datetime.date.today().year

idade = hoje-nasc

if idade == 18:
    print('É hora de se alistar!')
elif idade > 18:
    print(f'Já passou da hora de se alistar!\n'
          f'Você deveria ter se alistado em {(18-idade)+hoje}.')
else:
    print(f'Ainda não está na hora de se alistar.\n'
          f'Você deverá se alistar em {hoje-(idade-18)}.')