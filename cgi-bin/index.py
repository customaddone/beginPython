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
class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1

    # a - 1の場所にwを追加する
    def add(self, a, w):
        x = a
        while(x <= self.N):
            self.bit[x] += w
            x += x & -x

    # a未満の数字が何個あるか
    def get(self, a):
        ret, x = 0, a - 1
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    def cum(self, l, r):
        return self.get(r) - self.get(l)

    def lowerbound(self, w):
        if w <= 0:
            return 0
        x = 0
        k = self.b
        while k > 0:
            if x + k <= self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x + 1

# i < j, ai > ajとなるものの数は何個あるか
# 1, 2, 3...を順に置いていく
# 3個目を置こうとする時、盤面には１が２個置かれている
# 3が置かれている場所より前にi個置かれている場合、求めるものは2 - i個である

N = 4
A = [3, 1, 4, 2]
bit = BIT(N)

turn = [0] * N
# bitに１を置く時、その場所は1-indexになるので注意
for i in range(N):
    turn[A[i] - 1] = i + 1

ans = 0
for i in range(N):
    ans += i - bit.get(turn[i])
    bit.add(turn[i], 1)
    # 1を置く
    # [ , 1, , ]
    # 2を置く
    # [ , 1, , 2] 1は正常な位置にある
    # 3を置く
    # [3, 1, , 2] 1, 2が3より後ろにあるのでans += 2
    # 4を置く
    # [3, 1, 4, 2] 2が4より後ろにあるのでans += 1
print(ans)

# ARC031
N = 4
B = [2, 4, 1, 3]

# 各積み木は左か右かを選んで移動させられる
# BITの小さい方でいい
place = [0] * (N + 1)
for i in range(N):
    place[B[i]] = i

bit = BIT(N + 1)
# 左にある自分より小さいものではない（大きいもの）の数
left = [0] * (N + 1)
# 右にある自分より小さいものではない（大きいもの）の数
right = [0] * (N + 1)
for i in range(N, 0, -1):
    bit.add(place[i] + 1, 1)
    left[i] = bit.get(place[i] + 1)
    right[i] = (N - i) - bit.get(place[i] + 1)

ans = 0
for l, r in zip(left, right):
    # どちらか小さい方
    ans += min(l, r)
print(ans)
