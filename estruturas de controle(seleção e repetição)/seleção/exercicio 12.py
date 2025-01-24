mamifero = input("É mamífero? Sim ou não: ")
ave = input("É ave? Sim ou não: ")
repteis = input("É reptil? Sim ou não: ")


#mamíferos
if( (mamifero == 'Sim') or (mamifero == "sim")):
    quadrupede = input("É quadrupede? Sim ou não: ")
    bipedes = input("É bipede? Sim ou não: ")
    voadores = input("É voador? Sim ou não: ")
#######################################################################################################################################    
    if( (quadrupede == 'Sim') or (quadrupede == "sim")):
        carnivoro = input("É carnivoro? Sim ou não: ")
        if( (carnivoro == 'Sim') or (carnivoro == "sim")):
             print("Então o animal escolhido foi o Leão")
        else:
            herbivoro = input("É bipede? Sim ou não: ")
            if( (herbivoro == 'Sim') or (herbivoro == "sim")):
                print("Então o animal escolhido foi o Cavalo")
            else:
                 print("Não foi possivel determinar o animal escolhido")
#####################################################################################################################################                 
    if( (bipedes == 'Sim') or (bipedes == "sim")):
        onivoro = input("É bipede? Sim ou não: ")
        if( (onivoro == 'Sim') or (onivoro == "sim")):
            print("Então o animal escolhido foi o Homem")
        else:
            frutivoro = input("É bipede? Sim ou não: ")
            if( (frutivoro == 'Sim') or (frutivoro == "sim")):
                print("Então o animal escolhido foi o Macaco")
            else:
                 print("Não foi possivel determinar o animal escolhido")
#####################################################################################################################################
    if( (voadores == 'Sim') or (voadores == "sim")):
        print("Então o animal escolhido foi o Morcego")

        aquaticos = input("É bipede? Sim ou não: ")
    if( (aquaticos == 'Sim') or (aquaticos == "sim")):
        print("Então o animal escolhido foi o Baleia")


######################################Aves##################################################################################################
if( (ave == 'Sim') or (ave == "sim")):
    n_aves = input("É não voador? Sim ou não: ")
    nadadoras = input("É nadador? Sim ou não: ")
    rapina = input("É rapina? Sim ou não: ")
    if( (ave == 'Sim') or (ave == "sim")):
        tropical = input("É tropical? Sim ou não: ")
        if( (tropical == 'Sim') or (tropical == "sim")):
            print("Então o animal escolhido foi o Avestruz")
        else:
            polar = input("É polar? Sim ou não: ")
            if( (polar == 'Sim') or (polar == "sim")):
                print("Então o animal escolhido foi o Pinguim")
            else:
                print("Não foi possivel determinar o animal escolhido")
####################################################################################################################################
        if( (nadadoras == 'Sim') or (nadadoras == "sim")):
            print("Então o animal escolhido foi o Pato")
############################################################################################################################################           
        if( (rapina == 'Sim') or (rapina == "sim")):
            print("Então o animal escolhido foi o Aguia")

###############################Répteis###################################################################################################
if( (repteis == 'Sim') or (repteis == "sim")):
    casco = input("Tem casco? Sim ou não: ")
    carnivoro = input("É carnivoro? Sim ou não: ")
    s_patas = input("É carnivoro? Sim ou não: ")
    if( (casco == 'Sim') or (casco == "sim")):
        print("Então o animal escolhido foi uma Tartaruga")
################################################################################################################################################
    if( (carnivoro == 'Sim') or (carnivoro == "sim")):
        print("Então o animal escolhido foi um Crocodilo")
######################################################################################################################################################
    if( (s_patas == 'Sim') or (s_patas == "sim")):
        print("Então o animal escolhido foi uma Serpente")    
