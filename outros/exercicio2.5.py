ano_nascimento = int(input("Informe o ano de seus nascimento: "))

idade = 2024- ano_nascimento

if idade >= 18:
    print("Você ja pode votar e tirar a carteira de habilitação")
else:
        if idade >= 16 and idade < 18:
            print("Você ja pode votar, mas não pode tirar a carteira de motorista")
