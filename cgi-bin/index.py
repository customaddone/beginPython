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
from itertools import combinations, permutations, product
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
num = copy.deepcopy(A)

for i in range(1, N):
    num[i] += num[i - 1]

# + - + -
margin_1 = 0
num_1 = copy.deepcopy(num)
cnt_1 = 0
for i in range(N):
    num_1[i] += margin_1
    if i % 2 == 0:
        plus = max(1 - num_1[i], 0)
        num_1[i] += plus
        margin_1 += plus
        cnt_1 += plus
    else:
        minus = max(num_1[i] - (-1), 0)
        num_1[i] -= minus
        margin_1 -= minus
        cnt_1 += minus

margin_2 = 0
num_2 = copy.deepcopy(num)
cnt_2 = 0
for i in range(N):
    num_2[i] += margin_2
    if i % 2 != 0:
        plus = max(1 - num_2[i], 0)
        num_2[i] += plus
        margin_2 += plus
        cnt_2 += plus
    else:
        minus = max(num_2[i] - (-1), 0)
        num_2[i] -= minus
        margin_2 -= minus
        cnt_2 += minus

print(min(cnt_1, cnt_2))
