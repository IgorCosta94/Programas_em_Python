v1 = [0.0] * 10
v2 = [' '] * 10

for x in range(0,10,1):
    ponto = float(input("Informe a pontuação final da prova: "))
    nome = input("Informe o nome do candidato: ")
    if ponto > 70.0:
        v1[x] = ponto
        v2[x] = nome

print("Candidatos que obtiveram mais que 70 pontos na prova fina:")
for x in range(0,10,1):
    if v1[x] > 0.0:
        print(f"\tNome: {v2[x]}\tPontuação: {v1[x]}")

