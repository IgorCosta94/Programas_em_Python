n = int(input("Digite o termo da sequencia Fibonacci: "))
ant=0
b=1

for atual in range(2,n+1,1):
    fibo=ant+b 
    ant=b
    b=fibo
    print(fibo)

