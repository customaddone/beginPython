#https://atcoder.jp/contests/abc150/tasks/abc150_c
import itertools
n = int(input())
# itertools順列の中身はタプル
p = tuple(list(map(int, input().split())))
q = tuple(list(map(int, input().split())))
# listにする
# lista((1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1)...)の中の
# (1, 2, 3)とかを探す
lista = list(itertools.permutations(range(1, n + 1)))
print(abs(lista.index(p) - lista.index(q)))
