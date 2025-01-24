valor = float(input("Informe o valor da compra: "))

metodo_pag = int(input("Informe o metodo de pagamento(1,2,3 ou 4): "))

if metodo_pag == 1:
    total = valor - (valor * 0.10)
elif metodo_pag == 2:
    total = valor - (valor * 0.05)
elif metodo_pag == 3:
    total = valor
elif metodo_pag == 4:
   total = valor + (valor * 0.10)

print(f"Valor a ser pago: {total}")
