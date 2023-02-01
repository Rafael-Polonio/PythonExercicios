# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1s entre eles.

for c in range(10, 0, -1):
    print(c)
    from time import sleep
    sleep(1)
print('BUUUUUUM!!!!')