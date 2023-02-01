# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza.    Primeiro: Ana.  Último: Mária

n = str(input('Digite seu nome completo: '))

n = n.title().split()

n1 = n[0]
n2 = n[len(n)-1] #o [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante.

print(n1, n2)