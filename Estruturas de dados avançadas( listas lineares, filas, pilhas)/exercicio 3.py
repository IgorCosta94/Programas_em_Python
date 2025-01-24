#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
def parenteses():
    parab = []
    n = '1'
    
    print("Para terminar digite 0\n")
    
    while n != '0':
        n = input("Informe a sequência de parenteses: ")
        if n =='(' or n == ')':
            parab.append(n)
            
    comparacao(parab)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

def comparacao(w):
    cont = 0
    cont2 = 0
    for h in range(0,len(w) , 1):
        if w.pop() == '(':
            cont += 1
        else:
            cont2 += 1
        
    if cont == cont2:
        print("Os parênteses estão balanceados.")
    else:
        print("Os parênteses não estão balanceados")
        
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
        
parenteses()
