def combinacao(n_elemento, p_a_p):
    total_1 = 1
    total_2 = 1
    total_3 = 1
    elemento = n_elemento - p_a_p
    
    for w in range(1, n_elemento+1, 1):
        total_1 *= w
        print(total_1)
        print()
    for x in range(1, p_a_p + 1, 1):
        total_2 *= x 
        print(total_2)
        print()
        
    for y in range(1, elemento+1, 1):
        total_3 *= y
        print(total_3)
        print()
    total = total_1/((total_2)*(total_3))
    print(total)
    
elemento = int(input("Informe um número inteiro: "))
p = int(input("Informe um número inteiro: "))

combinacao(elemento, p)
