n = int(input())
lista = []
listb = []
ans = float('inf')

"""
for i in range(n):
    a, b = map(int, input().split())
    lista.append([a, b])
    listb.append(a)
    listb.append(b)
listb.sort()
for i in range(len(listb)):
    for j in range(i, len(listb)):
        sum = 0
        for k in range(n):
            sum += abs(lista[k][0] - listb[i]) + (lista[k][1] - lista[k][0]) + abs(lista[k][1] - listb[j])
        ans = min(ans, sum)
print(ans)
"""
