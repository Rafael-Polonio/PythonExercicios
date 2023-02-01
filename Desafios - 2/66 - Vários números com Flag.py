# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar '999', que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
contador = somatoria = 0
while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n == 999:
        break
    somatoria += n
    contador +=1
print('=-=-=-=-'*5)
print(f'{contador} números foram digitados, cuja somatória é {somatoria}')