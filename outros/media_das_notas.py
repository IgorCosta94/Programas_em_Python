contador=1
soma=0

while(contador<=4):
    n=float(input("Digite as notas do aluno. Digite uma por vez: "))
    soma+=n
    contador+=1

print("A média das notas do alunos é:",soma/4)
