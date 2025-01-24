pilhalocal = ["Ciclano","João"]
print(f"Tamanho: {len(pilhalocal)}, Fila: {pilhalocal}")
pilhalocal.extend(["Beltrano", "José"])

print(f"Tamanho: {len(pilhalocal)}, Fila: {pilhalocal}")
pilhalocal.append("Fulano")
print(f"Tamanho: {len(pilhalocal)}, Fila: {pilhalocal}")

while pilhalocal:
    print("Atendendo: ", pilhalocal.pop())
