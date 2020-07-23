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
import heapq
from math import sqrt
from fractions import gcd
import random
import string
import copy
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

N = getN()
que = [getList() for i in range(N)]

# もしwが同じならhが大きい順に（大→小へ更新していく）
que.sort(key = lambda i: i[1], reverse = True)
# wが小さい順に並ぶ
que.sort(key = lambda i: i[0])

h_list = []
for i in range(N):
    h_list.append(que[i][1])

def lis(A):
    L = [A[0]]
    for a in A[1:]:
        # Lの末尾よりaが大きければ増加部分を拡張できる
        if a > L[-1]:
            # 前から順にLに追加していく
            L.append(a)
        else:
            L[bisect_left(L, a)] = a

    # Lの配列の長さは求まる
    # Lの中身はデタラメ
    return len(L)
print(lis(h_list))

"""
# 最初から i 番目までの最大値を求めるだけで良いならBITを使える
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def ope(self, x, y):
        return max(x, y)

    def update(self, i, v):
        j = i
        while j <= self.n:
            self.data[j] = self.ope(self.data[j], v)
            j += j & -j

    def query(self, i):
        ret = 0
        j = i
        while 0 < j:
            ret = self.ope(self.data[j], ret)
            j &= (j - 1)
        return ret

bit = BIT(10 ** 5)

for w, h in que:
    # 高さh未満の箱が何個あるか(wは昇順にソートしてるので考える必要なし)
    # 最初は0個
    q = bit.query(h - 1)
    # 高さhの時の箱の数を更新
    # 箱の数がq + 1のものは高さがどんどん小さく更新されていく
    bit.update(h, q + 1)
print(bit.query(10 ** 5))
"""
