from dataclasses import dataclass
def reg():
    @dataclass
    
    class cheque:
        numero_cheque: int
        agencia: int
        numero_conta: int
        DV: int
        nome: str
        valor: float
        
    cont = 0
    x = [0] *100

    for w in range(0,len(x),1):
        x[w] = cheque(0,0,0,0,'',0.0)
    
    print("//Para encerrar digite 0 - zero para o número da conta//")
    print()
    
    numero_cheque = int(input("Informe o numero do cheque: "))
    
    while numero_cheque != 0 and cont < 100:
        
        agencia = int(input("Informe o numero da agência: "))
        numero_conta = int(input("Informe o numero da conta: "))
        
        DV = verificador(numero_conta)

        nome = input("Informe seu nome: ")
        valor = float(input("Informe o valor do cheque: "))

        x[cont] = cheque(numero_cheque,agencia,numero_conta,DV,nome,valor)
        print()

        print("//Para encerrar digite 0 - zero para o número da conta//")
        print()
        cont += 1
        numero_cheque = int(input("Informe o numero do cheque: "))
       

    mmmmm(x)


def verificador(x):
    s = x
    calculo = 0
    global cont
    cont = 0
    w = 0
    while x != 0:
        calculo = x % 10
        x = x // 10
        cont += 1
    return inverso(s,cont)
    
######################################################################################

def inverso(q,m):
    v=q
    w = pow(10,m-1)
    soma = 0
    while w != 0:
        calculo = q % 10
        cont = w * calculo
        soma += cont
        w = w // 10
        q = q // 10
    soma = soma + v
    return inverso2(soma)

#########################################################################################
    
def inverso2(r):
    x = r
    soma = 0
    cont = 0
    
    while x != 0:
        calculo = x % 10
        x = x // 10
        cont += 1
        
    while cont > 0:
        calculo = (r % 10) * cont
        soma +=calculo
        cont -= 1
        r = r // 10
    return soma

############################################################################################

def mmmmm(d):
    total = 0
    for w in range(0,len(d) - 1,1):
        for y in range(1,len(d),1):
            if d[w].nome == d[y].nome:
                total += d[w].valor
    print(f"Valor total: {total}")            



reg()
