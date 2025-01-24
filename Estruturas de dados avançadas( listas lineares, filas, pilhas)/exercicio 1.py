from collections import deque

fila =  deque( [3,9,5,1] )
#for w in range(0, 4, 1):
 #   n = int(input("Digite um número inteiro: "))
  #  fila.append(n)
print(fila)
print()

fila.append(2)

print("numero ", 2, " entrou na fila\n")
print(fila)
print()

print("numero ", fila.popleft(), " saiu da fila")
print("numero ", fila.popleft(), " saiu da fila")
print("numero ", fila.popleft(), " saiu da fila")

fila.append(7)

print("numero ", 7, " entrou na fila\n")
print(fila)
print()

print("numero ", fila.popleft(), " saiu da fila")
print("numero ", fila.popleft(), " saiu da fila")

fila.append(4)

print("numero ", 4, " entrou na fila\n")
print(fila)
print()

print("numero ", fila.popleft(), " saiu da fila")
print("numero ", fila.popleft(), " saiu da fila")

fila.append(8)

print("numero ", 8, " entrou na fila\n")
print(fila)
print()


fila.append(6)

print("numero ", 6, " entrou na fila\n")
print(fila)
print()

print("numero ", fila.popleft(), " saiu da fila")

print(fila)
print()
