# https://www.ioi-jp.org/joi/2008/2009-ho-prob_and_sol/2009-ho.pdf#page=4
# sysで入力の際のメモリ消費が軽減される
# MLE出るときに使って
import sys
from copy import deepcopy
from bisect import bisect_left
input = sys.stdin.readline

d = int(input())
n = int(input())
k = int(input())
lista = [0] + [int(input()) for i in range(n - 1)] + [d]
listb = [int(input()) for i in range(k)]
lista.sort()

ans = 0
for i in listb:
    # lista内で挟み込める位置を探す
    point = bisect_left(lista, i)
    # ここマイナスにならないよう注意
    ans += min(abs(i - lista[point - 1]), abs(lista[point] - i))
print(ans)
