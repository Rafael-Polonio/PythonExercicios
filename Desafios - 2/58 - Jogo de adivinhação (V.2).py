# Melhore o jogo do desafio 28, onde o computador vai pensar entre 1 e 10.
# Mas agora o jogador vai tentar advinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer
from random import randint
c = randint(1,10)
j = int(input('Aposte qual número inteiro entre 1 e 10 o computador sorteou: '))
print(c)
while not j == c:
    c = randint(1, 10)
    j = int(input('Você errou. Tente novamente: '))
    print(c)
    print('-=-=-='*5)
print(c)
print('Parabéns, você acertou!')