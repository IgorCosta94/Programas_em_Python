from collections import deque

filacliente = deque(["Ciclano","João"])
print(f"Tamanho: {len(filacliente)}, Fila: {filacliente}")
filacliente.extend(["Beltrano", "José"])

print(f"Tamanho: {len(filacliente)}, Fila: {filacliente}")
filacliente.append("Fulano")
print(f"Tamanho: {len(filacliente)}, Fila: {filacliente}")

while filacliente:
    print("Atendendo: ", filacliente.popleft())
