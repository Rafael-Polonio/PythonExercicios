# Crie um programa que leia vários números inteiros pelo teclado.
# No final, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
interruptor = 'n'
contadorvezes = v = vtotal = vmaior = vmenor = 0
while interruptor not in 'Ss':
    v = int(input('Digite um número inteiro: '))
    vtotal += v
    contadorvezes += 1
    if contadorvezes == 1:
        vmaior = v
        vmenor = v
    else:
        if v>vmaior:
            vmaior = v
        if v<vmenor:
            vmenor = v
    interruptor = str(input('Você quer parar de digitar valores? [S/N]')).upper().strip()
print('-=-=-='*5)
print(f'A média dos {contadorvezes} os valores lidos, cuja somatória é {vtotal}, é {vtotal/contadorvezes}.\n'
      f'O maior valor lido foi {vmaior}.\n'
      f'O menor valor lido foi {vmenor}.')
