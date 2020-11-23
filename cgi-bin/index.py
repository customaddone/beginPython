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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# ARC007 C - 節約生活

"""
最低限のテレビ数を求める
テレビの種類が1なので楽
最小1 ~ 最大10
最大の10から数を減らしていく
"""

C = [i == 'o' for i in input()]
N = len(C)

ans = float('inf')
for bit in range(1 << N): # 何台目を使うか
    cnt = 0
    judge = [0] * N
    for i in range(N):
        if bit & (1 << i):
            cnt += 1
            for j in range(N):
                # C[(j + i) % N]: ループしたC
                judge[j] |= C[(j + i) % N] # 0 |= 1 = 1, # 1 |= 1 = 1

    if sum(judge) == N:
        ans = min(ans, cnt)

print(ans)

# ABC002 派閥
# 条件
# n人の国会議員の集合A{A1, A2... An}の任意の二人i, jについて
# (i, j)がqueryに含まれる

# この人数nの最大値を求める

# 集合Aの取り方は？
# N <= 12なのでbit全探索で全ての集合について条件を満たすか判定できる
N, M = getNM()
mem = set()
for i in range(M):
    a, b = getNM()
    mem.add((a - 1, b - 1))

ans = 0
for bit in range(1 << N):
    # 任意のi, jについてqueryに含まれているか判定
    flag = True
    for i in range(N):
        for j in range(i + 1, N):
            # 適当に選んだ２人がbitの中に含まれていれば
            if bit & (1 << i) and bit & (1 << j):
                if not (i, j) in mem:
                    flag = False
    # もし集合bitが条件を満たすなら人数を調べる
    if flag:
        opt = bin(bit).count('1')
        ans = max(ans, opt)
print(ans)

# ABC018 D - バレンタインデー
N, M, P, Q, R = getNM()
que = []

# 女子N人の中からP人、男子M人の中からR人選ぶ
# 女子N人の中からP人選ぶ通りがNCR通り 最大18C9 = 役4万通り
# 男子についてもう4万通りを選ぶのは無理
# 逆に女子P人が選んだ時にチョコレートを選んで幸福度が最大になるようにしよう
# 男子y1がいれば += z1
# 男子y2がいれば += z2...

# 各通りについてチョコレート最大364通りを探索
# チョコciについて選んだ女子にxiがいる場合はyiに幸福度を追加（yiが選ばれる場合の幸福度）

for i in range(R):
    x, y, z = getNM()
    que.append([x - 1, y - 1, z])

def counter(array):
    girls = set(array)
    boys = [0] * M
    for x, y, z in que:
        if x in girls:
            boys[y] += z
    boys.sort(reverse = True)
    return sum(boys[:Q])

ans = 0
# 女子の全組み合わせを出す
def comb_pow(i, array):
    global ans
    if i == P:
        ans = max(ans, counter(array))
        return
    # ここの4を変えてrootを変更
    last = -1
    if len(array) > 0:
        last = array[-1]

    for j in range(last + 1, N):
        new_array = array + [j]
        comb_pow(i + 1, new_array)
comb_pow(0, [])
