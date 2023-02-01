# Crie um programa que leia 2 valores e mostre um menu na tela:
# 1 = somar;
# 2 = multiplicar;
# 3 = mostrar o maior valor;
# 4 = digitar novos números;
# 5 = sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.
escolha = 0
while escolha not in [5]:
    v1 = float(input('Digite um valor: '))
    v2 = float(input('Digite outro valor: '))
    escolha = int(input('O que você deseja fazer com esses valores:\n'
                        '1 = somar\n'
                        '2 = Multiplicar\n'
                        '3 = Mostrar qual o maior valor\n'
                        '4 = Reiniciar para digitar novos valores\n'
                        '5 = sair do programa'))

    if escolha in [1]:
        print(f' {v1} + {v2} = {v1+v2}')
    if escolha in [2]:
        print(f' {v1} * {v2} = {v1*v2}')
    if escolha in [3]:
        if v1 > v2:
            print(f'{v1} é o maior valor')
        else:
            print(f'{v2} é o maior valor')
    if escolha in [4]:
        print('Reset')
    print('-=-=-=-'*5)
print('Programa encerrado.')