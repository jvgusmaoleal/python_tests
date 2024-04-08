# Solicitar ao usuário
# -Número de BPM e Idade
# - Dentro, Fora e Abaixo

bpm = input("Informe o seu número de batimentos por minuto(BPM): ")
idade = input("Informe a sua idade: ")

#convertento para números inteiros
bpm = int(bpm)
idade = int(idade)
# realizando o teste lógicos 
if idade <= 2:
    if 120 <= bpm <= 140:
        print("Os batimentos estão dentro da faixa adequada.")
    elif bpm < 120:
        print("Os batimentos estão abaixo da faixa adequada.")
    else:
        print("Os batimentos estão acima da faixa adequada.")
elif 8 <= idade <= 17:
    if 80 <= bpm <= 100:
        print("Os batimentos estão dentro da faixa adequada.")
    elif bpm < 80:
        print("Os batimentos estão abaixo da faixa adequada.")
    else:
        print("Os batimentos estão acima da faixa adequada.")
elif idade >= 18:
    if 70 <= bpm <= 80:
        print("Os batimentos estão dentro da faixa adequada.")
    elif bpm < 70:
        print("Os batimentos estão abaixo da faixa adequada.")
    else:
        print("Os batimentos estão acima da faixa adequada.")
else:
    if 50 <= bpm <= 60:
        print("Os batimentos estão dentro da faixa adequada.")
    elif bpm < 50:
        print("Os batimentos estão abaixo da faixa adequada.")
    else:
        print("Os batimentos estão acima da faixa adequada.")