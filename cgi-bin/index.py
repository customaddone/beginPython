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

# ABC008 C - コイン
n = getN()
c = getArray(n)
sumans = 0

for i in c:
    lista = [j for j in c if i % j == 0]
    count = len(lista)
    sumans += math.ceil(count / 2) / count
print(sumans)

# ABC011 D - 大ジャンプ
def cmb_1(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

N, D = getNM()
X, Y = getNM()
X = abs(X)
Y = abs(Y)

# X軸に平行に正の向きに飛ぶ回数はx_time + α回
# X軸に平行に負の向きに飛ぶ回数はα回
x_time = X // D
y_time = Y // D

if X % D != 0 or Y % D != 0 or N < x_time + y_time:
    print(0)
    exit()

N_a = N - (x_time + y_time)
if N_a % 2 != 0:
    print(0)
    exit()
N_a //= 2

ans = 0
for i in range(N_a + 1):
    ans += cmb_1(N, x_time + i) * cmb_1(N - (x_time + i), i) * cmb_1(N - (x_time + 2 * i), y_time + N_a - i)
print(ans / (4 ** N))
