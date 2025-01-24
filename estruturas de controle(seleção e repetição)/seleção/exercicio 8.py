dia = int(input("Informe o dia de seu nascimento: "))
mes = int(input("Informe o mes de seu nascimento: "))
ano = int(input("Informe o ano de seu nascimento: "))

if((ano%4 == 0) and (mes == 2)):
    if(dia <= 29):
        print("Data válida para ano bissexto")
else:
    print("Data inválida para o ano bissexto")

if((ano%4 != 0) or (mes in [1,3,4,5,6,7,8,9,10,11,12])):        
    if((ano<=2024) and (ano >= 1997)):
        if mes in range(1,13):
            if(dia<=31):
                print("Data Valida")
    else:
        print("Data invalida")

        
if (mes == 1):
    if(dia>=21 and dia <=31):
       print("Aquário")
if (mes == 2):
    if(dia>=1 and dia <=18):
        print("Aquário")
if (mes == 2):
    if(dia>=19 and dia <=29):
        print("Peixes")
if (mes == 3):
    if(dia>=1 and dia <=20):
        print("Peixes")
if (mes == 3):
    if(dia>=21 and dia <=31):
        print("Aries")
if (mes == 4):
    if(dia>=1 and dia <=20):
        print("Aries")
if (mes == 4):
    if(dia>=21 and dia <=30):
        print("Touro")
if (mes == 5):
    if(dia>=1 and dia <=20):
        print("Touro")
if (mes == 5):
    if(dia>=21 and dia <=31):
        print("Gêmeos")
elif (mes == 6):
    if(dia>=1 and dia <=20):
        print("Gêmeos")
if (mes == 6):
    if(dia>=21 and dia <=30):
        print("Câncer")
if (mes == 7):
    if(dia>=1 and dia <=22):
        print("Câncer")
if (mes == 7):
    if(dia>=23 and dia <=31):
        print("Leão")
if (mes == 8):
    if(dia>=1 and dia <=22):
        print("Leão")
if (mes == 8):
    if(dia>=23 and dia <=31):
        print("Virgem")
if (mes == 9):
    if(dia>=1 and dia <=22):
        print("Virgem")
if (mes == 9):
    if(dia>=23 and dia <=30):
        print("Libra")
if (mes == 10):
    if(dia>=1 and dia <=22):
        print("Libra")
if (mes == 10):
    if(dia>=23 and dia <=31):
        print("Escorpião")
if (mes == 11):
    if(dia>=1 and dia <=21):
        print("Escorpião")
if (mes == 11):
    if(dia>=22 and dia <=30):
        print("Sagitário")
if (mes == 12):
    if(dia>=1 and dia <=21):
        print("Sagitário")
if (mes == 12):
    if(dia>=22 and dia <=31):
        print("Capricórnio")
if (mes == 1):
    if(dia>=1 and dia <=20):
        print("Capricórnio")
