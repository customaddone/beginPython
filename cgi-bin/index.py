n, k = map(int, input().split())
lista = []
listb = [0]

lista = list(map(int, input().split()))
for i in range(n):
    listb.append(lista[i] + listb[i])
print(lista)
print(listb)
