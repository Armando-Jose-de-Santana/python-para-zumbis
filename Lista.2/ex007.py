metros = int(input('Tamanho da área a ser pintada(m²): '))

if metros % 54 == 0:
    latas = metros / 54
else:
    latas = int(metros / 54) + 1

valor = latas * 80

print(f"""
Total de latas de tinta: {latas}
Preço total: R${valor:.2f}""")
