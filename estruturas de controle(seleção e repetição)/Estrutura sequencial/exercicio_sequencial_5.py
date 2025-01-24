ano_ani = int(input("Informe o ano do aniversário"))
dia_ani = int(input("Informe o dia do aniversário"))
mes_ani = int(input("Informe o mês do aniversário no formato(00)numérico"))

ano_atual = int(input("Informe o ano atual: "))
dia_atual = int(input("Informe o dia atual: "))
mes_atual = int(input("Informe o mês atual: "))

ano = ano_atual - ano_ani

dia = 365 * 30

mes = dia/12



print(f"Dias: {dia} Meses: {mes} Anos: {ano}")
