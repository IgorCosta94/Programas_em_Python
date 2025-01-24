Vlido = []
vpar = []
vimpar = []

for w in range(10):
    Vlido.append(int(input(f"Número {w + 1}: ")))

for w in range(10):
    if Vlido[w] % 2 == 0:
        vpar.append(Vlido[w])
    else:
        vimpar.append((Vlido[w]))

print(f"Vetor lido: {Vlido}")

print(f"Vetor Par, de tamanho {len(vpar)} : {vpar}")

print(f"Vetor impar, de tamanho {len(vimpar)}:{vimpar}")
