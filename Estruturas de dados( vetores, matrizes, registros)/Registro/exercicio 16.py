from dataclasses import dataclass
@dataclass
class contato:
    apelido: str
    nome: str
    telefone_f: int
    telefone_c: int

lista= [0] * 20
selecao = 10
contador = 0

print(" ----------------------")
print("| 0 - para sair        |\n| 1 - incluir contato  |\n| 2 - consultar contato|\n| 3 - lista de contatos| ")
print(" ----------------------")
selecao = int(input("Informe a opçao para o menu: "))

while selecao != 0:

    if (selecao == 1):
        if lista[contador] == 0 and contador < 20:
            lista[contador] = contato('','',0,0)
            lista[contador].apelido = input("Informe o apelido do contado: ")
            lista[contador].nome = input("Informe o nome do contato: ")
            lista[contador].telefone_f = int(input("Informe o telefone fixo do contado: "))
            lista[contador].telefone_c = int(input("Informe o telefone celular do contado: "))
        contador += 1
        
    if((selecao == 2) and (contador > 0)):
        apld = input("Para consultar o contato informe o apelido: ")
        for x in range(0, contador, 1):
            if(lista[x].apelido != apld):
                print("Pesquisando.....")
            if(lista[x].apelido == apld):
                print(f"Contato encontrado\nApelido: {lista[x].apelido}\nNome: {lista[x].nome}\nTelefone fixo: {lista[x].telefone_f}\n"
                      f"Telefone celular: {lista[x].telefone_c}\n")
                
    if ((selecao == 3)):
        print("||Lista de contatos||")
        for x in range(0, contador, 1):
            print(f"Apelido: {lista[x].apelido}\nNome: {lista[x].nome}\nTelefone fixo: {lista[x].telefone_f}\nTelefone celular: {lista[x].telefone_c}\n")
            

    print(" ----------------------")
    print("| 0 - para sair        |\n| 1 - incluir contato  |\n| 2 - consultar contato|\n| 3 - lista de contatos| ")
    print(" ----------------------")
    selecao = int(input("Informe a opçao para o menu: "))

print("PROGRAMA ENCERRADO!!!!")
