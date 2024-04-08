# Início
# 1) Estruturar a tabela de juros e quantidades de parcelas.
# 2) Coletar o valor da dívida.
# 3) Cacular e printa os valores devidos para cada opção de parcelamento.
# Fim


# Tabela de juros 
juros_por_parcela = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

# Coleta do valor da dívida
valor_divida = float(input("Digite o valor da dívida: "))

# Calcula e exibe as informações para cada opção de parcelamento
for parcelas, taxa_juros in juros_por_parcela.items():
    juros = valor_divida * (taxa_juros / 100)
    valor_total = valor_divida + juros
    valor_parcela = valor_total / parcelas
    print("Total:R$ {:,.2f} Juros:R$ {:,.2f} Número de parcelas:{} Valor da Parcela:R$ {:,.2f}".format(
        valor_total, juros, parcelas, valor_parcela))
