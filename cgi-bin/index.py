from operator import mul
from functools import reduce

n = int(input())
a = list(map(int, input().split()))

def cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


lista = [0] * (n + 1)
sum = 0
for j in range(n):
    lista[a[j]] += 1
for i in lista:
    if i >= 2:
        sum += cmb(i, 2)
for i in a:
    print(sum - lista[i] + 1)
