anos = 0
sentinela = 0
anacleto = 1.50
felisberto = 1.10

while sentinela != -1:

    if felisberto > anacleto:
        sentinela = -1
        
    anacleto += 0.02
    felisberto += 0.03
    anos += 1

print(f"A quantidade de anos para Felisberto ficar maior que Anacleto é : {anos} anos")
    
