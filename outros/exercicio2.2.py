x1 = int(input("Primeiro numero: "))
x2 = int(input("Segundo numero: "))
x3 = int(input("Terceiro numero: "))

if x1 > x2 and x1 > x3:
    print(x1)
    
    if x2 > x3 :
        print(x2)
        print(x3)
        
    else:
        print(x3)
        print(x2)
        
else:
    if x2 > x1 and x2 > x3:
        print(x2)
        
        if x1 > x3:
            print(x1)
            print(x3)
            
        else:
            print(x3)
            print(x1)
            
    else:
        if x3 > x1 and x3 > x2:
            print(x3)
            
            if x1 > x2:
                print(x1)
                print(x2)
                
            else:
                print(x2)
                print(x1)
