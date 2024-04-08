# variáveis
#     idade: inteiro
#     rm: alfanumérico
#     autorizado: caractere
# início
#     Escreva “Por favor, digite seu nome”
#     Leia rm
#     Escreva “Por favor, digite sua idade”
#     Leia idade
#     Se idade >=18 então
#         Escreva “Sua participação foi autorizada, aluno de RM”, rm
#               Escreva “Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!”
#           Senão
#               Escreva “Você possui autorização dos responsáveis para participar? S – SIM ou N – NÃO”
#               Leia autorizado
#               Se autorizado = “S” então
#             Escreva “Sua participação foi autorizada, aluno de RM”, rm
#                   Escreva “Mais instruções serão enviadas ao email dos seus responsáveis”
#               Senão
#             Escreva “Sua participação não foi autorizada por causa da sua idade”
#         Fim_se
#           Fim_se
# Fim

nome = input("Por favor, digite seu nome: ")
idade = input("Por favor, digite sua idade: ")
rm = input("Por favor, digite seu RM: ")
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}".format((rm)))
    print("Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!")
else:
    autorizado = input("Você possui autorização dos responsáveis para participar? S – SIM ou N – NÃO")
    if autorizado == 'S':
        print("Sua participação foi autorizada, aluno de RM {}".format(int(rm)))
        print("Mais instrJuções serão enviadas ao seu e-mail cadastrado na FIAP!")
    else:
        print("Sua participação não foi autorizada por causa da idade")

