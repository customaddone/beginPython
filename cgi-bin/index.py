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

# 重複なし
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

# rand_dist
def rand_dist(ransize, rantime):
    dist_alta = []
    while len(dist_alta) < min(rantime, ransize * (ransize - 1) // 2):
        a, b = rand_ints_nodup(0, ransize - 1, 2)
        if not [a, b] in dist_alta:
            dist_alta.append([a, b])
    return sorted(dist_alta)
print(rand_dist(4, 5))

# rand_letter
def rand_letter(size):
    ascii_original='ATCG'
    digits_original='01'

    digits='0123456789'
    ascii_lowercase='abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # 好きなものを使ってね
    psuedo = ascii_original

    return ''.join([random.choice(psuedo) for i in range(size)])
print(rand_letter(12))

# 使い方
# ABC006 C - スフィンクスのなぞなぞ
N = rand_N(5, 10)
M = rand_N(10, 30)
print(N)
print(M)

for l in range(1, N):
    for m in range(1, N):
        for n in range(1, N):
            if 2 * l + 3 * m + 4 * n == M and l + m + n == N:
                print(l, m, n)
