#################################################################################################
                                                                                                #
homens = []                                                                                     #
mulheres = []                                                                                   #
cont = 0                                                                                        #
                                                                                                #
#################################################################################################
                                                                                                #
def lista_H(hom):                                                                               #
                                                                                                #
    hom.append(input("Digite um nome para homens: "))                                           #
def lista_M(mum):                                                                               #
    mum.append(input("Digite um nome para mulheres: "))                                         #
                                                                                                #
#################################################################################################
                                                                                                #
def opcoes(hom,mum):                                                                            #
                                                                                                #
    opcs = int(input("Digite 1 para exclusão, 2 para localização e 3 para alteração\n"))        #
    if opcs == 1:                                                                               #
        exclusao(hom,mum)                                                                       #
    elif opcs == 2:                                                                             #
        localizacao(hom,mum)                                                                    #
    elif opcs == 3:                                                                             #
        alteracao(hom,mum)                                                                      #
                                                                                                #
#################################################################################################        
def exclusao(hom,mum):                                                                          #
                                                                                                # 
    sinalizador = 0                                                                             #
    h_ou_m = int(input("Digite 1 para homem ou 2 para mulher: "))                               #
    nome = input("Forneça o nome que deseja excluir: ")                                         #
                                                                                                #
    if h_ou_m == 1:                                                                             #
        for w in range(0,len(hom)-1,1):                                                         #
                                                                                                #
            if nome == hom[w]:                                                                  #
                hom.remove(hom[w])                                                              #
                sinalizador = 1                                                                 #
                                                                                                #
        if sinalizador == 1:                                                                    #
            print("O Nome foi excluido com sucesso\n")                                          #
                                                                                                #
        elif sinalizador == 0:                                                                  #
            print("Nome não encontrado!!! Não foi possivel excluir\n")                          #
                                                                                                #
    elif h_ou_m == 2:                                                                           #
        for w in range(0,len(mum)-1,1):                                                         #
                                                                                                #
            if nome == mum[w]:                                                                  #
                mum.remove(mum[w])                                                              #
                sinalizador = 1                                                                 #
                                                                                                #
        if sinalizador == 1:                                                                    #
            print("O Nome foi excluido com sucesso\n")                                          #
                                                                                                #
        elif sinalizador == 0:                                                                  #
            print("Nome não encontrado!!! Não foi possivel excluir\n")                          #
#################################################################################################
                                                                                                #
def localizacao(hom,mum):                                                                       #
    h_ou_m = int(input("Digite 1 para homem ou 2 para mulher: "))                               #
    nome = input("Forneça o nome que deseja localizar: ")                                       #
                                                                                                #
    if h_ou_m == 1:                                                                             #
        for w in range(0,len(hom)-1,1):                                                         #        
                                                                                                #
            if nome == hom[w]:                                                                  #
                print(f"O nome: {nome} esta na {hom.index(nome)} posição\n")                    #
                sinalizador = 1                                                                 #
                                                                                                #
        if sinalizador == 1:                                                                    #
            print("O Nome foi localizado\n")                                                    #
        elif sinalizador == 0:                                                                  #
            print("O Nome não foi localizado\n")                                                #
                                                                                                #
    elif h_ou_m == 2:                                                                           #
        for w in range(0,len(mum)-1,1):                                                         #
                                                                                                #
            if nome == mum[w]:                                                                  #
                print(f"O nome: {nome} esta na {mum.index(nome)} posição\n")                    #
                sinalizador = 1                                                                 #
                                                                                                #
        if sinalizador == 1:                                                                    #
            print("O Nome foi localizado\n")                                                    #
        elif sinalizador == 0:                                                                  #
            print("O Nome não foi localizado\n")                                                #
                                                                                                #
#################################################################################################
                                                                                                #        
def alteracao(hom,mum):                                                                         #
    h_ou_m = int(input("Digite 1 para homem ou 2 para mulher: "))                               #
    nome = input("Forneça o nome que deseja alterar: ")                                         #
    nome2 = input("Forneça o novo nome que deseja substituir : ")                               #
                                                                                                #
    if h_ou_m == 1:                                                                             #
        for w in range(0,len(hom)-1,1):                                                         #
                                                                                                #
            if nome == hom[w]:                                                                  #
                hom.remove(hom[w])                                                              #
                hom.insert(w,nome2)                                                             #
                sinalizador = 1                                                                 #
                                                                                                #
        if sinalizador == 1:                                                                    #
            print("O Nome foi substituido com sucesso\n")                                       #
                                                                                                #
        elif sinalizador == 0:                                                                  #
            print("O Nome não foi substituido\n")                                               #
                                                                                                #   
    elif h_ou_m == 2:                                                                           # 
        for w in range(0,len(mum)-1,1):                                                         #   
                                                                                                #
            if nome == mum[w]:                                                                  #
                mum.remove(mum[w])                                                              #
                mum.insert(w,nome2)                                                             #
                sinalizador = 1                                                                 #
                                                                                                #   
        if sinalizador == 1:                                                                    #
            print("O Nome foi substituido com sucesso\n")                                       #
                                                                                                #
        elif sinalizador == 0:                                                                  #
            print("O Nome não foi substituido\n")                                               #
                                                                                                #
#################################################################################################
                                                                                                #    
while cont <= 5:                                                                                #
    h_ou_m = int(input("Digite 1 para homem ou 2 para mulher: "))                               #
    if h_ou_m == 1:                                                                             #
        lista_H(homens)                                                                         #        
    elif h_ou_m == 2:                                                                           #
        lista_M(mulheres)                                                                       #
    cont += 1                                                                                   #
                                                                                                #
#################################################################################################
                                                                                                #
opcoes(homens,mulheres)                                                                         #
print(homens)                                                                                   #
print()                                                                                         #    
print(mulheres)                                                                                 #    
                                                                                                #
#################################################################################################
