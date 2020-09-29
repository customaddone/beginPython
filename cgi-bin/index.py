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
mod = 998244353

#############
# Main Code #
#############

# ABC161 E - Yutori
"""
N日間のうちK日選んで働く
働いたらそれからC日間は働かない
Sにxがついていたら働かない

oの付いてる日のみ働く
全ての通りを求めてみよう

N, K, C = 11, 3, 2
S = ooxxxoxxxoo の時
働けるのは[1, 2, 6, 10, 11]日目
ここから3つ以上間が空く条件で3つ選ぶと条件を満たす
全ての通りでi日目に働く必要がある

A = [1, 2, 5, 7, 11, 13, 16]
M = 4
C = 3

for bit in range(1 << len(A)):
    cnt = []
    for i in range(len(A)):
        if bit & (1 << i):
            cnt.append(A[i])
    if len(cnt) == 4:
        for i in range(1, len(cnt)):
            if cnt[i] - cnt[i - 1] <= C:
                break
        else:
            print(cnt)

# python index.py
[1, 5, 11, 16]
[1, 7, 11, 16]
[2, 7, 11, 16]

A = [1, 2, 5, 10, 24]
M = 3
C = 2
[1, 5, 10]
[2, 5, 10]
[1, 5, 24]
[2, 5, 24]
[1, 10, 24]
[2, 10, 24]
[5, 10, 24]
[1, 5, 10, 24] M + 1回以上ジャンプできる場合には答えが[]になる
A[0]から頑張ってもM回しかジャンプできない

間がC + 1以上離れたM個の集合はどのように求める？
必ず働く日の特性は？
動かすと？
場所は固定？
"""
# N, K, C = getNM()
# S = getN()

N, K, C = getNM()
S = input()

# i回目に選べる要素の上限と下限を比べる
place = []
for i in range(N):
    if S[i] == 'o':
        place.append(i)

# 下限 出来るだけ前の仕事を選べるように
fore = [place[0]]
for i in place[1:]:
    if i - fore[-1] > C:
        fore.append(i)

# 上限 出来るだけ後ろの仕事を選ぶように
back = deque([])
back.append(place[-1])
for i in place[::-1]:
    if back[0] - i > C:
        back.appendleft(i)
back = list(back)

if len(fore) != K:
    print()
    exit()

ans = []
for a, b in zip(fore, back):
    if a == b:
        ans.append(a + 1)

for i in ans:
    print(i)


"""
fore = [0] * N
if S[0] == 'o':
    fore[0] = 1

for i in range(1, N):
    fore[i] = fore[i - 1]
    if S[i] == 'o' and i - C - 1 >= 0:
        fore[i] = max(fore[i], fore[i - C - 1] + 1)

back = [float('inf')] * N
ma = max(fore)
if S[N - 1] == 'o':
    back[N - 1] = ma

for i in range(N - 2, -1, -1):
    back[i] = min(ma, back[i + 1])
    if S[i] == 'o' and i + C + 1 < N:
        back[i] = min(back[i], back[i + C + 1] - 1)
print(back)
"""
