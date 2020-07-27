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
from math import sqrt, pi
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
