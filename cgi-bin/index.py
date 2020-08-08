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

M = 4
N = 5
maze = [
[1, 0, 0, 1],
[0, 1, 1, 0],
[0, 1, 1, 0],
[1, 0, 0, 1]
]

def changer(o, f):
    for i in range(1, M):
        for j in range(N):
            # 一つ上のmazeとflipを調べる
            # mazeが黒 and flipが偶数回ひっくりかえる or mazeが白 and flipが奇数回ひっくりかえるなら
            if (maze[i - 1][j] == 1) ^ (f[i - 1][j] % 2):
                o[i][j] += 1
                f[i][j] += 1
                f[i - 1][j] += 1
                if j >= 1:
                    f[i][j - 1] += 1
                if j < N - 1:
                    f[i][j + 1] += 1
                if i < M - 1:
                    f[i + 1][j] += 1

    return o, f

# １行目について全探索
for bit in range(1 << N):
    opt = [[0] * N for i in range(M)]
    flip = [[0] * N for i in range(M)]
    for i in range(N):
        if bit & (1 << i):
            opt[0][i] += 1
            flip[0][i] += 1
            if i >= 1:
                flip[0][i - 1] += 1
            if i < N - 1:
                flip[0][i + 1] += 1

    opt, flip = changer(opt, flip)

    # 最後の列について判定
    for j in range(N):
        # 違うなら
        if (maze[M - 1][j] == 1) ^ (flip[M - 1][j] % 2):
            break
    else:
        print(opt)
