# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto;
# à vista no cartão: 5% de desconto;
# em até 2x no cartão: preço normal;
# em até 3x no cartão: 20% de juros.

p = float(input('Preço original do produto: '))
met = int(input('Método de pagamento:\n'
                '[1] à vista em dinheiro\n'
                '[2] à vista no cartão\n'
                '[3] em até 2x no cartão\n'
                '[4] em até 3x no cartão\n'
                'Qual é sua opção? '))

if met == 1:
    print(f'Seu desconto será de 10%, isto é, {p*0.1} reais\n'
          f'Portanto o produto custará {p-(p*0.1)}')
if met == 2:
    print(f'Seu desconto será de 5%, isto é, {p*0.05} reais\n'
          f'Portanto o produto custará {p-(p*0.05)} reais')
if met == 3:
    print(f'Sem desconto. O preço do produto é {p}')
if met == 4:
    print(f'juros de 20%, sendo 3 parcelas de {p*0.20} reais, o que totalizará {(p*0.20)*3} reais em júros.\n'
          f'Somando os júros, o produto custará {p+((p*0.20)*3)} reais.')