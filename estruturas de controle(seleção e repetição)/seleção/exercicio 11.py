pais = input("Informe o nome do pais: ")
medalhas_o = int(input("Informe a quantidade de medalhas de ouro: "))
medalhas_p = int(input("Informe a quantidade de medalhas de prata: "))
medalhas_b = int(input("Informe a quantidade de medalhas de bronze: "))
total_pais = ((medalhas_o * 3) + (medalhas_p * 2) + (medalhas_b * 1))   
 
pais2 = input("Informe o nome do pais: ")
medalhas_2o = int(input("Informe a quantidade de medalhas de ouro: "))
medalhas_2p = int(input("Informe a quantidade de medalhas de prata: "))
medalhas_2b = int(input("Informe a quantidade de medalhas de bronze: "))
total_pais2 = (medalhas_2o * 3) + (medalhas_2p * 2) + (medalhas_2b * 1)  

pais3 = input("Informe o nome do pais: ")
medalhas_3o = int(input("Informe a quantidade de medalhas de ouro: "))
medalhas_3p = int(input("Informe a quantidade de medalhas de prata: "))
medalhas_3b = int(input("Informe a quantidade de medalhas de bronze: "))
total_pais3 = (medalhas_3o * 3) + (medalhas_3p * 2) + (medalhas_3b * 1)

if total_pais > total_pais2 and total_pais > total_pais3:
    print(f"{pais} ficou em primeiro lugar")
    if total_pais2 > total_pais3:
        print(f"{pais2} ficou em segundo lugar")
    else:
        print(f"{pais3} ficou em segundo lugar")
        print(f"{pais2} ficou em terceiro lugar")

if total_pais2 > total_pais and total_pais2 > total_pais3:
    print(f"{pais2} ficou em primeiro lugar")
    if total_pais > total_pais3:
        print(f"{pais} ficou em segundo lugar")
    else:
        print(f"{pais3} ficou em segundo lugar")
        print(f"{pais} ficou em terceiro lugar")


if total_pais3 > total_pais and total_pais3 > total_pais:
    print(f"{pais3} ficou em primeiro lugar")
    if total_pais > total_pais2:
        print(f"{pais} ficou em segundo lugar")
    else:
        print(f"{pais2} ficou em segundo lugar")
        print(f"{pais} ficou em terceiro lugar")
