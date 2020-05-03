# https://atcoder.jp/contests/abc006/tasks/abc006_4
from bisect import bisect_left
n = int(input())
lista = [int(input()) for i in range(n)]

# 最長増加部分列問題 (LIS)の問題
def lis(A):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            L.append(a)
        # このelseに引っかかった時にトランプのソートが必要
        else:
            L[bisect_left(L, a)] = a
    return len(L)
print(n - lis(lista))
