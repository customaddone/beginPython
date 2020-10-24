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

# ARC039 C - 幼稚園児高橋君

"""
訪問してない格子点とは？
どんどん掘り進んでいく感覚
ぐるぐるするのか？
現在の上下左右の領域を保持するか？
順番は関係ない？
URL
RLU 関係はある

同じ点には戻らない
dequeする？
Dancing Links
4近傍の情報を抑えておく

現在の場所について、次の場所の情報を
次の場所について、その場所に行った場合の逆方向の次の場所の情報を抑える
"""

K = getN()
S = input()
D = 'URDL'
dxy = [(0,1), (1,0), (0,-1), (-1,0)] # 上下左右
nxs = {}

# for i in range(4):
#     dx, dy = dxy[i]
for di, (dx,dy) in enumerate(dxy):
    nxs[(0, 0, di)] = (dx, dy) # (x座標, y座標, どの方向？): (次のx座標、次のy座標)

x = y = 0
for c in S:
    i = D.index(c) # 直進する方向
    # 上下左右４箇所について次の場所がレコードされているか
    # されていなければ作る
    for di, (dx, dy) in enumerate(dxy): # 4方向について探索
        # 順方向について
        if (x, y, di) not in nxs: # 探索してなければ
            ddx, ddy = dxy[di]
            nxs[(x, y, di)] = (x + ddx, y + ddy) # 現在の座標 + 1を追加
        # 逆方向について
        dj = (di + 2) % 4
        if (x, y, dj) not in nxs: # 探索してなければ
            ddx, ddy = dxy[dj]
            nxs[(x, y, dj)] = (x + ddx, y + ddy)

        nx, ny = nxs[(x, y, di)] # 次の場所
        nxs[(nx, ny, dj)] = nxs[(x, y, dj)] # 次の場所について、逆方向の次の場所は現在の場所についての逆方向の次の場所と同じ
    x, y = nxs[(x, y, i)] # 新しい場所に移動

print(x, y)
