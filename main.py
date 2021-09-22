salarioHora = float(input('Quanto você ganha por hora? '))
horasTrabalhadas = int(input('Quantas horas você trabalha por mês? '))
salarioBruto = salarioHora*horasTrabalhadas
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print('Seu salário bruto é: ', salarioBruto)
print('Você paga: ', impostoRenda,' de imposto de renda.')
print('Você paga: ', inss, 'de INSS.')
print('Você paga: ', sindicato, 'de sindicato.')
print('Seu salário bruto é: R$', salarioLiquido)