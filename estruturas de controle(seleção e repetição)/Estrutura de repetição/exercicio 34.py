idade = int(input("Informe sua idade: "))
opiniao = input("Qual sua opinião sobre o filme?\n'O' - Ótimo\n'B' - Bom\n'C' - Regular\n'R' - Ruim\n'E' - Péssimo\nRespota: ")
print("\nPARA ENCERRAR DIGITE -1 PARA IDADE\n")

cont_O = 0
cont_B = 0
cont_R = 0
cont_T = 0
cont_E = 0
cont_idade = 0
acum_idadeO = 0
acum_idadeR = 0
acum_idadeE = 0

while idade != -1:
    if opiniao == 'O':
        cont_O += 1
        if idade > acum_idadeO:
            acum_idadeO = idade
            
    elif opiniao == 'B':
        cont_B += 1
        
    elif opiniao == 'R':
        cont_R += 1
        cont_idade += idade
        if idade > acum_idadeR:
            acum_idadeR = idade
            
    elif opiniao == 'E':
        cont_E += 1
        if idade > acum_idadeE:
            acum_idadeE = idade


    cont_T += 1

    idade = int(input("Informe sua idade: "))
    opiniao = input("Qual sua opinião sobre o filme?\n'O' - Ótimo\n'B' - Bom\n'C' - Regular\n'R' - Ruim\n'E' - Péssimo\nRespota: ")
    print("\nPARA ENCERRAR DIGITE -1 PARA IDADE\n")

print(f"A quantidade de respostas Ótimo foi de: {cont_O}")
print(f"A diferença percentual entre respostas bom e ruim é de: {((cont_B * 100) /cont_T) - ((cont_R * 100)/cont_T)}")
print(f"A porcentagem de respostas Péssimo foi de: {(cont_E * 100) /cont_T }\nÉ a maior idade entre respostas Péssimo é de: {acum_idadeE}")
print(f"A diferença entre a maior idade que respondeu ótimo e ruim é de: {acum_idadeO - acum_idadeR}")
    
