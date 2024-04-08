quantos_alimentos_dia= int(input("Quantos alimentos foram cosumidos dia: "))
total_de_calorias = 0
for alimento in range(1, quantos_alimentos_dia + 1):
    caloria = int(input("Informe a quatidade de calorias do alimento {}: ".format(alimento)))
    total_de_calorias = total_de_calorias + caloria

print("-> O total de calorias consumidas no dia foi de: {} kcal".format(total_de_calorias))