idade = int(input("Informe a sua idade: "))

if (idade <16):
    print(f"Menores de 16 anos não votam. Sua idade é {idade}")
else:
    if((idade >=18) and (idade<=65)):
        print(f"Eleitor obrigatorio. Sua idade é {idade}")
    else:
        if((idade >=16 and idade < 18) or (idade > 65)):
            print(f"Eleitor facultativo. Sua idade é {idade}")
