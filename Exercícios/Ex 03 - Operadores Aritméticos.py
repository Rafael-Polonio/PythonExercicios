n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
div = n1 / n2
m = n1 * n2
pot = n1 ** n2
divi = n1 // n2

print(f'a soma é {s},\na subtração {sub},\na divisão {div:.2f}\ne a multiplicação é {m}', end=' ')
print(f'a potência é {pot} \ne a divisão inteira é {divi}')