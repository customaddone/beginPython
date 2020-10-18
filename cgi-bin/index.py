def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

# ARC126 F - XOR Matching
# d = 2 ** N - 1について
# 1 xor 2 xor... xor dは
# 各桁にフラグが2 * (N - 1)本ずつ立っている（つまり0になる）
# なのでXを抜くとXを構成する部分についてフラグが抜けてXができる

M, K = getNM()

if M == 0 and K == 0:
    print(0, 0)

elif M == 1 and K == 0:
    print(0, 0, 1, 1)

elif M >= 2 and K < 2 ** M:
    ans = []
    for n in range(2 ** M):
        if n != K:
            ans.append(n)
    print(*ans, K, *ans[::-1], K)

else:
    print(-1)

# B - Median Pyramid Easy

"""
頂点にXを書き込む
N段目の順列としてありうるものを示す
・一番都合のいいものを出す
・条件を緩和してみる
・条件が小さい場合を考える
Xがなければ
2 ** (N - 2)を頂点に書けばいい これ以外不可能ってことはない？
N = 4の場合
   4
  345
 23456
1234567

・実験
def cnt(array):
    alta = deepcopy(array)
    while len(alta) > 1:
        l = []
        for i in range(1, len(alta) - 1):
            l.append(sorted([alta[i - 1], alta[i], alta[i + 1]])[1])
        alta = l
    return alta[0]

A = [1, 2, 3, 4, 5]
for i in permutations(A):
    print(i, cnt(i))
X = 2, 3, 4なら可能
同様に N = 4なら 2 ~ 6であれば可能

X = 2の場合 最終的に上がってくるのは2, 2, 3
1, 2がペアで存在する場合はX = 2になる？
上にあげるには？
上げたい数を真ん中で二つ並べることができたら（例:6 4 2 2 3)勝ち確

真ん中に X + 2, X - 1, X, X + 1, X - 2を配置
これを中央の値と入れ替える
"""

def cnt(array):
    alta = deepcopy(array)
    while len(alta) > 1:
        l = []
        for i in range(1, len(alta) - 1):
            l.append(sorted([alta[i - 1], alta[i], alta[i + 1]])[1])
        alta = l
    return alta[0]

N, X = getNM()
ma = 2 * N
mid = ma // 2
if X == 1 or X == ma - 1:
    print('No')
    exit()
print('Yes')

list = [i for i in range(ma - 1, 0, -1)]
ans = [-1] * ma

if (ma - 1) - X > 1 and mid - 2 > 0: # X + 2を入れ替える
    ans[mid - 2] = list.pop(list.index(X + 2))
if X - 2 > 0 and (ma - 1) - mid > 1: # X - 2を入れ替える
    ans[mid + 2] = list.pop(list.index(X - 2))

ans[mid - 1] = list.pop(list.index(X - 1))
ans[mid + 1] = list.pop(list.index(X + 1))
ans[mid] = list.pop(list.index(X))

for i in range(1, ma):
    if ans[i] == -1:
        ans[i] = list.pop()

for i in ans[1:]:
    print(i)
