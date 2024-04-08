# Início 
# 0- Preparo do ambiente para receber os dados
# 1-Preciso colotar a informação de quantos funcionarios vão participar da votação.
# 2-Configurar a estrutura de votação com base no numero de votantes
# 3-Contagem dos votos 
# 4- Imprima o resultado da votação !
# Fim



# 0) Prepara o programa para a coleta de dados:
# Números representando dias
votos = {
    1: 0,  # segunda-feira
    2: 0,  # terça-feira
    3: 0,  # quarta-feira
    4: 0,  # quinta-feira
    5: 0   # sexta-feira
}

# Mapeamento dos números para os dias semanais para o print no final
dias_da_semana = {
    1: "segunda-feira",
    2: "terça-feira",
    3: "quarta-feira",
    4: "quinta-feira",
    5: "sexta-feira"
}

# 1) Coleta do n de votantes 
n_de_votantes = int(input("Informe quantas pessoas irão participar da votação: "))

# 2) Estrutura de repetição com base no n de votantes
for _ in range(n_de_votantes):
    voto = int(input("Digite 1 para segunda, 2 para terça, 3 para quarta, 4 para quinta, 5 para sexta: "))
    while voto not in votos:
     print("Opção inválida. Por favor, escolha um número entre 1 e 5.")
     voto= int(input("Digite 1 para segunda, 2 para terça, 3 para quarta, 4 para quinta, 5 para sexta: "))
    votos[voto] += 1

# Contagem dos votos
dia_escolhido = max(votos, key=votos.get)
qtd_votos = votos[dia_escolhido]

# Impressão do resultado
print("O dia escolhido para a live foi {}, com {} votos.".format(dias_da_semana[dia_escolhido], qtd_votos))

 