# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
c = random.randint(0,5)

j = int(input('Aposte contra a máquina um número entre 0 e 5: '))

from time import sleep
print('Processando...')
sleep(2) #a função spleep da biblioteca time faz com que o computador "durma" por x tempo; gera um delay

if c==j:
    print('Parabéns, você venceu!')
else:
    print('Derrotado')
    print(f'A máquina jogou {c}')