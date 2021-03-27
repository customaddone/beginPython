from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

N, A = getNM()
w = []
v = []
for i in range(N):
    o_v, o_w = getNM()
    w.append(o_w)
    v.append(o_v)

# 半分全列挙 + 二分探索
def half_knapsack(N, limit, weight, value):
    # 半分全列挙
    L, R = [[0, 0]], [[0, 0]]
    for w, v in zip(weight[:15], value[:15]):
        for i in range(len(L)):
            L.append([w + L[i][0], v + L[i][1]])

    for w, v in zip(weight[15:], value[15:]):
        for i in range(len(L)):
            R.append([w + R[i][0], v + R[i][1]])
    R.sort()
    R_w, R_v = [R[i][0] for i in range(len(R))], [R[i][1] for i in range(len(R))]

    ans = 0
    for w, v in L:
        if w > limit:
            continue
        o = R_v[bisect_right(R_w, limit - w) - 1]
        if ans < v + o:
            ans = v + o

    return ans



# あるweightで獲得できる最大のvalue
def knapsack_wei(N, limit, weight, value):
    dp = [[0] * (limit + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(limit + 1):
            if weight[i] <= j:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i])
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[N][limit]

# あるvalueを獲得するために必要な最小のweight
def knapsack_val(N, limit, weight, value):
    max_v = sum(value)
    dp = [[float('inf')] * (max_v + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(max_v + 1):
            if value[i] <= j:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - value[i]] + weight[i])
            else:
                dp[i + 1][j] = dp[i][j]
    for i in range(max_v - 1, -1, -1):
        if dp[N][i] <= limit:
            return i

if N <= 30:
    print(half_knapsack(N, A, w, v))
    exit()
elif max(w) <= 1000:
    print(knapsack_wei(N, A, w, v))
    exit()
else:
    print(knapsack_val(N, A, w, v))
    exit()
