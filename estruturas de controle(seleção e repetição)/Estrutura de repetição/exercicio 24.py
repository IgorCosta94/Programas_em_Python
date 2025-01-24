comp = 0.0
cont_g = 0
cont_m = 0
cont_f = 0
cont_f_med = 0
######################################################################################
for x in range(1,11,1):
    sexo = input("Informe o sexo 'M' para masculino e 'F' para feminino: ")
    altura = float(input("Informe a altura da pessoa: "))
    
    cont_g += 1
    
    if altura > comp:
        comp = altura
        
    if ((sexo == 'M') or (sexo == 'm')):
        cont_m += 1
    elif((sexo == 'F') or (sexo == 'f')):
        cont_f += 1
        cont_f_med += altura

######################################################################################
percentual_m = (cont_m*100)/cont_g
percentual_f = (cont_f*100)/cont_g
print(f"A maior altura do grupo é {comp}")
print(f"A media de altura das mulheres é {cont_f_med / cont_f}")
print(f"O número de homens é {cont_m}")
print(f"A diferença percentual de homens e mulheres é de {percentual_m - percentual_f}%")
