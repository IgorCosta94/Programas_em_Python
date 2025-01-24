print("Para encerrar digite 0 em coódigo da empresa: ")
codigo = int(input("Informe o código da empresa: "))
n_funcionarios = int(input("Informe o número de funcionarios: "))
porte = input("Informe o porte da empresa")


nf_g = 0
nf_m = 0
nf_p = 0
nf_mc = 0
cg = 0
cm = 0
cp = 0
cmc = 0

while codigo != 0:
    if porte == "Grande" or porte == "grande":
        if n_funcionarios > nf_g:
            nf_g = n_funcionarios
            cg = codigo
    elif porte == "Media" or porte == "media":
        if n_funcionarios > nf_m:
            nf_m = n_funcionarios
            cm = codigo
    elif porte == "peguena" or porte == "Pequena":
        if n_funcionarios > nf_p:
            nf_p = n_funcionarios
            cp = codigo
    elif porte == "Micro" or porte == "micro":
        if n_funcionarios > nf_mc:
            nf_mc = n_funcionarios
            cmc = codigo
    else:
        print("Informe o porte da empresa correto(grande,media,pequena ou micro\n")

        
    print("Para encerrar digite 0 em coódigo da empresa: ")
    codigo = int(input("Informe o código da empresa: "))
    n_funcionarios = int(input("Informe o número de funcionarios: "))
    porte = input("Informe o porte da empresa")

print("=================")
print(f"Grande Porte\nnCodigo:{cg}\nN_funcionarios:{nf_g}\n=================")
print(f"Medio Porte\nCodigo:{cm}\nN_funcionarios:{nf_m}\n=================")
print(f"Pequeno Porte\nnCodigo:{cp}\nN_funcionarios:{nf_p}\n=================")
print(f"Micro Porte\nCodigo:{cmc}\nN_funcionarios:{nf_mc}")


















