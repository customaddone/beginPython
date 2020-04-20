from operator import mul
from functools import reduce
n, a, b = map(int, input().split())
mod = 10 ** 9 + 7

def cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

print(2 ** n - cmb(n, a) - cmb(n, b) - 1)
