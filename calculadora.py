# algoritmo "Soma"
# variáveis
#     valor1, valor2, soma, divisao, subtracao, multiplicacao: real
# início
#     Escreva "Digite o primeiro valor"
#     Leia valor1
#     Escreva "Digite o segundo valor"
#     Leia valor2
#     soma = valor1 + valor2
#     Escreva "A soma é ", soma
#     subtracao = valor1 - valor2
#     Escreva "A soma é ", subtracao
#     divisao = valor1 / valor2
#     Escreva "A soma é ", divisao
#     multiplicacao = valor1 * valor2
#     Escreva "A soma é ", multiplicacao
# Fim

valor1 = input("Por favor digite o primeiro valor: ")
valor2 = input("Por favor digite o segundo valor: ")
soma = float(valor1) + float(valor2)
print("A soma é {}".format(soma))
subtracao = float(valor1) - float(valor2)
print("A subtração é {}".format(subtracao))
divisao = float(valor1) / float(valor2)
print("A divisão é {}".format(divisao))
multiplicacao = float(valor1) * float(valor2)
print("A multiplicação é {}".format(multiplicacao))
