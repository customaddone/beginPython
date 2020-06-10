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
import math
from fractions import gcd
import random
import string
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

N = getN()
A = getList()

r, tmp = 0, A[0]
# l:左端
cnt = 0
for l in range(N):
    # rを1進めたときにA[N - 1]以内に収まる　かつ　問題の条件を満たすなら
    while r + 1 < N and tmp ^ A[r + 1] == tmp + A[r + 1]:
        # 右端を伸ばす
        tmp += A[r + 1]
        r += 1
    # 計算
    cnt += r - l + 1

    # r == N - 1（最後まで）に達していないかつl == r（進めなかった）とき
    if r + 1 < N and l == r:
        r += 1
        # 新しいtmp = A[r + 1]をセットする
        tmp = A[r]
    else:
        # 左端が1進むと同時にtmpの左端の分を削る
        tmp -= A[l]
print(cnt)
