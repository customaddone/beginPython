import sys
# 再帰制限を外す
sys.setrecursionlimit(1000000)
lista = [0] * 10000

def fib(n):
    if lista[n] != 0:
        return lista[n]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    lista[n] = fib(n - 1) + fib(n - 2)
    return lista[n]
n = int(input())
print(fib(n))
