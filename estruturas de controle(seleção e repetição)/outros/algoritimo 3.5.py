n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

ma = (n1+n2+n3+n4)/4

print(ma)

if( ma >= 7):
    print("Aluno aprovado")
    print("Parabens")
else :
    print("Aluno reprovado")
    print("Estude mais")
