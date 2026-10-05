from datetime import datetime

hoje = datetime.now().date()
print("Este sistema calcula o valor de juros de um produto.\n")
valor_produto = float(input("Digite o valor do produto: \n"))
data_vencimento = input("Digite a data de vencimento do produto (formato: dd/mm/aaaa): \n")
data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y").date()
diferenca_dias = abs(hoje - data_vencimento).days
juros = 0.025

juros_ajustados = juros * diferenca_dias
valor_final = valor_produto + juros_ajustados

print(f"O valor final do produto com juros é: R$ {valor_final:.2f}")