a = input("Digite algo: ")
# a é um objeto

print('É numérico?', a.isalnum())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Só tem espaços?', a.isspace())
print('Só há maiúsculas?', a.isupper())
print('Só há minúsculas?', a.islower())
print('Está capitalizada, i.e., só a 1ª letra é maiúscula?', a.istitle())

# as funções "is..." são métodos