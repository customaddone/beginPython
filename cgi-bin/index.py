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

# ABC038 D-プレゼント
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
    bit.update(h, q + 1)
print(bit.query(10 ** 5))

# ABC140 E - Second Sum
# [Pl, Pr]間で２番目に大きいものの総和を
# l, rについてのnC2通りの全てについて求めよ

# 8 2 7 3 4 5 6 1
# 8 2: 2
# 8 2 7: 7
# 2 7 3: 3
# 8を含むもの（７通り）について2が２番目になるもの、7が２番目になるもの...
# 2を含むものについて（６通り）について7が...をそれぞれO(1)で求められれば

# N <= 10 ** 5
# Piが２番目になる通りが何通り　みたいな感じで求められる？
# Piが２番目になる条件　→　自分より上位のものを一つだけ含む

# ヒープキューとか使える？
# 二つ数字を入れる　→　最小値を取り出せばそれは２番目の数字
# 尺取り使える？

# 累積？　一番

class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1

    def add(self, a, w):
        x = a
        while(x <= self.N):
            self.bit[x] += w
            x += x & -x

    def get(self, a):
        ret, x = 0, a - 1
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    def cum(self, l, r):
        return self.get(r) - self.get(l)

    def lowerbound(self,w):
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

N = getN()
P = getList()
dic = {}
bit = BIT(N)
for i in range(N):
    dic[P[i]] = i + 1

# 両端に何もない時用
# [0] + Pの各要素 + [N + 1]みたいになる
dic[0] = 0
dic[N + 1] = N + 1
ans = 0

for i in range(N, 0, -1):
    # 8のインデックス、7のインデックス...に1を登録していく
    bit.add(dic[i], 1)
    # 左側にある既に登録したもの（自分より大きいもの + 自分）の数を数える
    c = bit.get(dic[i] + 1)
    # l1: 左側にある既に登録したもの（自分より大きいもの）のうち、一番右にあるもの
    # l2: l1の一つ左側にあるもの
    l1, l2 = bit.lowerbound(c - 1), bit.lowerbound(c - 2)
    # r1: 右側にある既に登録したもの（自分より大きいもの）のうち、一番左にあるもの
    # r2: r1の一つ右側にあるもの
    r1, r2 = bit.lowerbound(c + 1), bit.lowerbound(c + 2)
    S = (l1 - l2) * (r1 - dic[i]) + (r2 - r1) * (dic[i] - l1)
    ans += S * i
print(ans)

# ABC174 F - Range Set Query

# 色の種類
# 同じ色のボールがある場合、どの情報があれば良いか
# 最もrに近いボールの位置がわかればいい
N, Q = getNM()
C = getList()
que = []
for i in range(Q):
    l, r = getNM()
    que.append([i, l, r])

que_list = [[] for i in range(N + 1)]
for i in range(Q):
    que_list[que[i][2]].append(que[i])

c_place = [-1] * (max(C) + 1)
bit = BIT(N + 1)

ans = [0] * Q
for i in range(1, N + 1):# 1-indexなので　配列参照する際はi - 1

    if c_place[C[i - 1]] == -1: # 新規
        c_place[C[i - 1]] = i
        bit.add(i, 1)
    else: # 更新
        bit.add(c_place[C[i - 1]], -1)
        c_place[C[i - 1]] = i
        bit.add(i, 1)

    if len(que_list[i]) > 0: # i == rのqueryに答える
        for index, l, r in que_list[i]:
            ans[index] = bit.cum(l, r + 1)

for i in ans:
    print(i)

# ARC031 C - 積み木
# 反転数を求める感じで
N = getN()
B = getList()

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

# ARC033 C - データ構造
# 座圧BIT
Q = getN()
que = [getList() for i in range(Q)]

# データに入れる数字を抽出する
A = []
for t, x in que:
    if t == 1:
        A.append(x)
# 座標圧縮
# alter: A[i] → alt_A[i]
# rev: alt[i] → A[i]
def compress(array):
    s = set(array)
    s = sorted(list(s))
    alter = {}
    rev = {}
    for i in range(len(s)):
        alter[s[i]] = i
        rev[i] = s[i]

    return alter, rev

alter, rev = compress(A)

limit = Q + 1
bit = BIT(limit)
for t, x in que:
    if t == 1:
        bit.add(alter[x] + 1, 1)
    else:
        # xを超えないギリギリの場所が1-indexで与えられる
        opt = bit.lowerbound(x) - 1
        # 1-indexなのでそのままprintする
        print(rev[opt])
        # xを超えないギリギリの場所の一つ右を-1する
        bit.add(opt + 1, -1)
