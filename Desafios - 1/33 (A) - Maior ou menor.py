#faça um programa que leia 3 números e mostre qual é o maior e qual é o menor
n1 = float(input("insira um número: "))
n2 = float(input("insira outro número: "))
n3 = float(input("insira mais um número: "))
#print("aaa" if n1>n2 else "n2 é maior que n1", ", mas n3 é maior que n2" if n3>n2 else "e menor que n3, então n2 é o maior número")
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print("o maior valor é {}".format(maior))
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print("o menor valor é {}".format(menor))
