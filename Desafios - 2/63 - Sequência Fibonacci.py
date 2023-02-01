# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma sequência de fibonacci.
# Ex: 7 --->  0 1 1 2 3 5 8  (mostrou os 7 primeiros termos de fibonnacci)
ntermos = int(input('Digite o número de termos da sequência fibonacci: '))
t1 = 0
t2 = 1
print(f'{t1} --> {t2}', end='')
c = 3 # porque o primeiro e segundo termos já foram definidos, então começa no 3.
while c <= ntermos:
    t3 = t1 + t2
    print(f' --> {t3}', end='')
    t1 = t2
    t2 = t3
    c +=1