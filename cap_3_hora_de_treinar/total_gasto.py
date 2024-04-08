quantas_transacoes = int(input("Quantas transacoes vc realizou: "))
total_gasto = 0

for n_gasto in range(1, quantas_transacoes + 1,1):
    valor_gasto = float(input("Qual o valor da transação ({}): ".format(n_gasto)))
    total_gasto = total_gasto + valor_gasto
    media = total_gasto / n_gasto

print("O valor total de todas as trasações é: R$ {}. A média por gasto foi de: R$ {} ".format(total_gasto, media))    