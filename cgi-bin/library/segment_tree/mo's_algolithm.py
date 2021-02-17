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

#####func#####
def func(x, y):
    return bisect_left(x, y + 1) # y以下のものの個数を答える
#################

class SRD:
    def __init__(self, array, func):
        self.func = func
        self.n = len(array)
        self.num = array
        self.sN = int(self.n ** 0.5) + 1
        self.index = [i * self.sN - 1 for i in range(self.sN + 1)]
        self.bucket = [sorted(self.num[i * self.sN: min(self.n, (i + 1) * self.sN)]) for i in range(self.sN)]

    # 区間[left, right)についてtarget以上/以下のものの個数を求める
    def query(self, left, right, target):
        if left == right:
            return 0

        if left > right:
            left, right = right, left
        # leftとrightはどのバケットにある？
        left_border = bisect_left(self.index, left)
        right_border = bisect_left(self.index, right - 1)

        res = 0
        # left_borderとright_borderが同じ区間内にいる場合は
        if left_border == right_border:
            for i in range(left, right):
                res += func([self.num[i]], target)
            return res
        # left_borderとright_borderが同じ区間内にいない場合は
        # はみ出した部分について
        for i in range(left, min(self.n, self.index[left_border] + 1)):
            res += func([self.num[i]], target)
        # print(res)
        for i in range(self.index[right_border - 1] + 1, right):
            res += func([self.num[i]], target)
        # print(res)
        # バケット部分について
        for i in range(left_border, right_border - 1):
            res += func(self.bucket[i], target)
        # print(res)

        return res

# 計算量はO(nlogn + m√log1.5n)らしい
N, M = 7, 3
A = [1, 5, 2, 6, 3, 7, 4]
max_A = max(A)
que = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

sr = SRD(A, func)

for l, r, k in que:
    ng = 0
    ok = max_A + 1

    while ok - ng > 1:
        mid = (ng + ok) // 2
        # 少なすぎる場合は
        if sr.query(l - 1, r, mid) < k:
            # midを上げる
            ng = mid
        else:
            ok = mid
    # i - 1以下の数がL個、i以下の数がR個あり,
    # L < k <= Rなら
    # L-1  L  | L+1..k...R
    # i-1 i-1 |  i   i   i
    # となるのでokが答え
    print(ok)
