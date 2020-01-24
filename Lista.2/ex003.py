peso_dos_peixes = float(input('Digite a pesagem total de peixes: '))

multa = 0

if peso_dos_peixes > 50:
    excedente = peso_dos_peixes - 50
    multa = excedente * 4
else:
    multa = excedente = 0

print(f'Multa: R${multa:.2f}')
print(f'Total excedido(kg): {excedente:.2f}')
