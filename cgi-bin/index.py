# 全通り調べる
import itertools
n = int(input())
lista = []
ans = 10000000
for i in range(n):
    dist = list(map(int, input().split()))
    lista.append(dist)
for i in itertools.permutations(range(n)):
    time = 0
    for j in range(n - 1):
        time += lista[i[j]][i[j + 1]]
    ans = min(ans, time)
print(ans)
