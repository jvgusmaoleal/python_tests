# Início
# 1) Solicitamos ao usuário o valor do carro.
# 2) Calculamos o preço à vista aplicando o desconto de 20%.
# 3) Usamos tabela acréscimos para mapear
#  a quantidade de parcelas ao percentual de acréscimo correspondente.
#  Iteramos sobre esta tabela de precos
#  para calcular e exibir o preço final com acréscimo e o valor de cada parcela,
#  formatando a saída para ficar alinhada e clara.
# Fim

# 0) Tabela de acrescimos 
acrescimos = {
    6: 3,
    12: 6,
    18: 9,
    24: 12,
    30: 15,
    36: 18,
    42: 21,
    48: 24,
    54: 27,
    60: 30
}

# Coleta do preço do carro
valor_do_carro = float(input("Digite o valor do carro: "))

# Calcula o preço à vista 
valor_a_vista = valor_do_carro * 0.8

# Imprime o preço à vista
print("\nO preço final à vista com desconto 20% é: R${:,.2f}".format(valor_a_vista))

# Itera sobre a tabela de acrescimos
for parcelas, acrescimo in acrescimos.items():
    valor_total_parcelado = valor_do_carro * (1 + acrescimo / 100)
    valor_parcela = valor_total_parcelado / parcelas
    print("O preço final parcelado em {} X é de R${:,.2f} com parcelas de R${:,.2f}".format(parcelas, valor_total_parcelado, valor_parcela))
