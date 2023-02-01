from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
c = randint(0,2)
print('0 = Pedra\n1 = Papel\n2 = Tesoura')
j = int(input('Qual é a sua jogada?'))

print('-='*11)
print(f'O jogador escolheu {itens[j]}')
print(f'O computador escolheu {itens[c]}')
print('-='*11)

if c==0:
    if j==0:
        print(f'Empate ente {itens[j]} e {itens[c]}')
    elif j==1:
        print(f'Você ganhou. {itens[j]} ganha de {itens[c]}')
    elif j==2:
        print(f'Você perdeu. {itens[j]} perde para {itens[c]}.')
    else:
        print('Jogada invalida')
elif c==1:
    if j==0:
        print(f'Você perdeu. {itens[j]} perde para {itens[c]}.')
    elif j==1:
        print(f'Empate entre {itens[j]} e {itens[c]}')
    elif j==2:
        print(f'Você ganhou. {itens[j]} ganha de {itens[c]}')
    else:
        print('Jogada invalida')
elif c==2:
    if j==0:
        print(f'Você ganhou. {itens[j]} ganha de {itens[c]}')
    elif j==1:
        print(f'Você perdeu. {itens[j]} perde para {itens[c]}')
    elif j==2:
        print(f'Empate entre {itens[j]} e {itens[c]}')
    else:
        print('Jogada invalida')