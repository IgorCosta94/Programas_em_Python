def extenso(numero):
    if numero >= 1 and numero <= 999999:
        x = ['','Um','Dois','Três','Quatro','Cinco','Seis','Sete','oito','Nove','Dez',
             'onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte',
             'Trinta','Quarenta','Quinta','Sessenta','Setenta','Oitenta','Noventa','Cem']
        
        if numero <= 20:
            print(f"{x[numero]}")
        elif numero > 20 and numero < 30:
            print(f"{x[20]} e {x[numero%10]}")

        if numero == 30:
            print(f"{x[21]}")
        elif numero > 30 and numero < 40:
            print(f"{x[21]} e {x[numero%10]}")
        
        if numero == 40:
            print(f"{x[22]}")
        elif numero > 40 and numero < 50:
            print(f"{x[22]} e {x[numero%10]}")

        if numero == 50:
            print(f"{x[23]}")
        elif numero > 50 and numero < 60:
            print(f"{x[23]} e {x[numero%10]}")

        if numero == 60:
            print(f"{x[24]}")
        elif numero > 60 and numero < 70:
            print(f"{x[24]} e {x[numero%10]}")

        if numero == 70:
            print(f"{x[25]}")
        elif numero > 70 and numero < 80:
            print(f"{x[25]} e {x[numero%10]}")

        if numero == 80:
            print(f"{x[26]}")
        elif numero > 80 and numero < 90:
            print(f"{x[26]} e {x[numero%10]}")

        if numero == 90:
            print(f"{x[27]}")
        elif numero > 90 and numero < 100:
            print(f"{x[27]} e {x[numero%10]}")

        if numero == 100:
            print(f"{x[28]}")
        elif numero > 100 and numero < 120:
            print(f"{x[28]} e {x[numero%100]}")

    else:
        print("ERRO!!!NÚMERO FORA DO INTERVALO...")
        

n = int(input("Informe um numero no intervalo de 1 a 999.999: "))
extenso(n)
