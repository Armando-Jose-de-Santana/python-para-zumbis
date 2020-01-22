salário = float(input('Informe o salário: '))
percentagem = float(input('Informe a percentagem de aumento: '))
novo_salário = salário + (salário * percentagem / 100)

print(f'O salário de R${salário:.2f} com {percentagem}% de aumento é R${novo_salário:.2f}')
