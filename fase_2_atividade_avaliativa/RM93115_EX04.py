# Início
# 1) Solicita:
#        o tipo de investimento,
#        o valor a ser resgatado e
#        o número de dias investido.
# 2) Valida o tipo de investimento (1, 2 ou 3)
# 3) Se precisar: calcular a alíquota do IR com base no tempo de investimento.
# 4) Print do valor do imposto de renda a ser pago
#    ou
#    informa se é isento.
# Fim

# Coleta as informações do usuário
tipo_de_investimento = int(input("Digite o tipo de investimento (1 para CDB, 2 para LCI, 3 para LCA): "))
valor_do_resgate = float(input("Digite o valor a ser resgatado: "))
dias_investidos = int(input("Digite o número de dias que o valor permaneceu investido: "))

# Valida o tipo de investimento
if tipo_de_investimento not in [1, 2, 3]:
    print("Tipo de investimento inválido.")
else:
    if tipo_de_investimento == 1:
        if dias_investidos <= 180:
            aliquota_ir = 22.5
        elif 181 <= dias_investidos <= 360:
            aliquota_ir = 20
        elif 361 <= dias_investidos <= 720:
            aliquota_ir = 17.5
        else:
            aliquota_ir = 15

        # Calculo do valor do IR
        valor_ir = valor_do_resgate * (aliquota_ir / 100)
        print("O valor do imposto de renda sobre o resgate é: R$ {:.2f}".format(valor_ir))
    else:
        # Isentos de IR (LCI e LCA)
        print("O investimento escolhido é isento de imposto de renda.")

