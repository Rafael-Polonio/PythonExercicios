# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor '999', que é a condição de parada.
# No final, mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag, isto é, o '999')
v = vtotal = tentativas = totcaract = contcaract = conversor = 0
while not v == 999:
    v = int(input('Digite um valor inteiro: '))
    vtotal += v
    tentativas += 1
    conversor = str(v)
    contcaract = len(conversor.strip())
    totcaract += contcaract
print('-=-=-'*5)
print(f'Foram necessárias {tentativas-1} tentativas para que o programa se encerrasse.\n'
      f'A somatória de todos os números tentatos é {vtotal-999}.\n'
      f'Foram contabilizados {totcaract-3} caracteres utilizados no total.')
