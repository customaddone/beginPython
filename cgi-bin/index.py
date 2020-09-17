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


num = [2, 4, 6, 8]
limit = 10

def part_bitset1(num, limit):
    N = len(num)
    dp = 1 # 最初の0

    for i in range(N):
        dp |= (dp << num[i])

    return bin(dp)

max_diff = 30

def part_bitset2(num, limit):
    N = len(num)
    dp = 1 << max_diff # 最初の0
    print(bin(dp))

    for i in range(N):
        # +, -を加える
        dp |= (dp << num[i]) | (dp >> num[i])

    return dp

l = part_bitset2(num, limit)
ans = []
for i in range(l.bit_length()):
    if l & (1 << i):
        ans.append(i - max_diff)
# [-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(ans)

# ABC147 E - Balanced Path

MAX_DIFF = 80
h, w = getNM()

A = [getList() for i in range(h)]
B = [getList() for i in range(h)]
c = [[abs(A[i][j] - B[i][j]) for j in range(w)] for i in range(h)]

# bitset高速化
# 集合を010110...の形で持つ
sets = [[0 for j in range(w)] for i in range(h)]
# 中央0: 1 << MAX_DIFFに + c[0][0], - c[0][0]
sets[0][0] = (1 << MAX_DIFF + c[0][0]) | (1 << MAX_DIFF - c[0][0])

# 縦方向に進む
for i in range(1, h):
    # c[i][0]の+-を足したもの
    sets[i][0] |= (sets[i - 1][0] << MAX_DIFF + c[i][0]) | (sets[i - 1][0] << MAX_DIFF - c[i][0])
# 下方向に進む
for i in range(1, w):
    sets[0][i] |= (sets[0][i - 1] << MAX_DIFF + c[0][i]) | (sets[0][i - 1] << MAX_DIFF - c[0][i])
for i in range(1, h):
    for j in range(1, w):
        sets[i][j] |= (sets[i - 1][j] << MAX_DIFF + c[i][j]) | (sets[i - 1][j] << MAX_DIFF - c[i][j])
        sets[i][j] |= (sets[i][j - 1] << MAX_DIFF + c[i][j]) | (sets[i][j - 1] << MAX_DIFF - c[i][j])

# 終点の集合を見る
s = bin(sets[h - 1][w - 1] + (1 << (h + w) * MAX_DIFF))
min_diff = 1 << MAX_DIFF
for i in range(len(s)):
    if s[- 1 - i] == '1': # フラグが立っているなら判定
        min_diff = min(min_diff, abs(i - (h + w - 1) * MAX_DIFF))
print(min_diff)
