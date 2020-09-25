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

# ABC027 C - 倍々ゲーム
# ２人が最善を尽くす時、どちらが勝つか
# パターン1:ある状態になるように収束させれば必ず勝つ
# パターン2:ある場所を目指せば必ず勝つようになる
# パターン3:最初の配置のためどんな方法を取っても必ず勝つ

# まずは全通り試してみる　その中で勝ちが偏っている部分がある
N = getN()
k = N
depth = 0
while k > 1:
    k //= 2
    depth += 1
x = 1
cnt = 1
if depth % 2:
    while x <= N:
        if cnt % 2:
            x *= 2
        else:
            x *= 2
            x += 1
        cnt += 1
    if cnt % 2:
        print("Takahashi")
    else:
        print("Aoki")
else:
    while x <= N:
        if cnt % 2:
            x *= 2
            x += 1
        else:
            x *= 2
        cnt += 1
    if cnt % 2:
        print("Takahashi")
    else:
        print("Aoki")

# ABC048 D - An Ordinary Game
# 最終的にどのような形で終わるか
S = input()
if (S[0] != S[-1]) ^ (len(S) % 2):
    print('Second')
else:
    print('First')

# ABC059 D - Alice&Brown
# まずは全通り試してみる

# 最終形をイメージする →
# 1 0 操作出来ない　終わり
# 1 1 操作出来ない　終わり
# 逆に2 0 や 3 0 なら操作できる
# 2以上開く、０か１開くを繰り返す
X, Y = getNM()
X = int(X)
Y = int(Y)

if (X - Y) ** 2 > 1:
    print("Alice")
else:
    print("Brown")
