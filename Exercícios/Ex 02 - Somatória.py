n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
# se não especificasse que é "int", supororia "str" e, portanto, não seria uma somatória, mas uma conglomeração!!!

s = n1 + n2

# Sintaxe poluída --> print('a soma entre', n1,'e',n2, 'vale:', s)

print('a soma entre {} e {} vale: {}'.format(n1,n2,s))

# Ou (sintaxe novissima...)

print(f'a soma entre {n1} e {n2} vale {s}')