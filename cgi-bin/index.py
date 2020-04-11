import itertools
n = int(input())
# itertools順列の中身はタプル
p = tuple(list(map(int, input().split())))
q = tuple(list(map(int, input().split())))
# listにする
lista = list(itertools.permutations(range(1, n + 1)))
print(abs(lista.index(p) - lista.index(q)))
