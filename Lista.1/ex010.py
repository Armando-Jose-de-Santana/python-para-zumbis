cigarros = int(input('Quantos cigarros fuma por dia? '))
anos = int(input('Fumante durante quantos anos? '))

total_de_cigarros = anos * 365 * cigarros
dias_perdidos = total_de_cigarros * 10 / 24

print(f'Dias perdidos: {dias_perdidos:.2f}')
