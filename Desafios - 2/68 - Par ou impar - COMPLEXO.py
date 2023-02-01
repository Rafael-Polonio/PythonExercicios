# Faça um programa que jogue par ou impar com o computador.
# O jogo será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

vitorias = 0
while True:
    jogador = str(input('Par ou Ímpar: [P/I]')).upper().strip()[0]
    while jogador not in 'PI':
        jogador = str(input('Par ou Ímpar: [P/I]')).upper().strip()[0]
    njogador = int(input('Digite um número entre 1 e 5 a ser jogado: '))
    while njogador not in range (1,6):
        njogador = int(input('Digite um número entre 1 e 5 a ser jogado: '))
    computador = randint(1,5)
    parouimpar = computador + njogador
    print('-=-=-=-='*5)
    if jogador == 'P':
        if parouimpar%2==0:
            vitorias +=1
            print(f'O computador jogou {computador} e você jogou {njogador}\n'
                  f'cuja somatória ({parouimpar}) é um número Par, portanto)')
            print('Você ganhou! Jogue novamente.')
        else:
            print(f'O computador jogou {computador} e você jogou {njogador}\n'
                  f'cuja somatória ({parouimpar})é um número impar, portanto')
            print('Você perdeu.')
            break
    elif jogador == 'I':
        if parouimpar%2==1:
            print(f'O computador jogou {computador} e você jogou {njogador}\n'
                  f'cuja somatória ({parouimpar})é um número impar, portanto')
            print('Você ganhou. Jogue novamente')
        else:
            print(f'O computador jogou {computador} e você jogou {njogador}\n'
                  f'cuja somatória ({parouimpar})é um número par, portanto')
            print('Você perdeu.')
            break
print(f'Você perdeu. \n'
      f'Seu número de vitórias consecutivas foi {vitorias}')

