# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%;
# Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Valor do salário: '))
if s>1250:
    a1 = s*(10/100)
    print(f'Seu aumento será de 10%, que corresponde em termos absolutos a {a1:.2f} reais\n'
          f'Portanto, seu salário será {s+a1:.2f}')
else:
    a2 = s*(15/100)
    print(f'Seu aumento será de 15%, que corresponde em termos absolutos a {a2:.2f} reais\n'
          f'Portanto, seu salário será {s+a2:.2f}')