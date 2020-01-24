salário_hora = float(input('Quanto você ganhar por hora? R$ '))
horas_trabalhadas = float(input('Horas trabalhadas no mês: '))

salário_bruto = salário_hora * horas_trabalhadas
imposto_de_renda = salário_bruto * 0.11
inss = salário_bruto * 0.08
sindicato = salário_bruto * 0.05
salário_líquido = salário_bruto - imposto_de_renda - inss - sindicato

print(f"""
+ Salário Bruto   R${salário_bruto:.>32.2f}
- IR(11%)         R${imposto_de_renda:.>31.2f}
- INSS(8%)        R${inss:.>31.2f}
- Sindicato(5%)   R${sindicato:.>31.2f}
= Salário Líquido R${salário_líquido:.>32.2f}""")
