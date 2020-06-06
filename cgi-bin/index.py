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

# -2進数　N = -9のとき
# -9を1, -2, 4, -8...で表現する → 1 + (-10) を1, -2, 4, -8...で表現する
# -10を-2, 4, -8...で表現する
# ↑　使う数に1を加えないと-9を-2, 4, -8...で表現する事になりこれは不可能
def minus_digit(rev_n):
    if rev_n == 0:
        print('0')
        return

    cnt = 0
    rep = rev_n
    lista = []

    while rep != 0:
        split = (abs(rep) % 2 ** (cnt + 1)) // 2 ** cnt
        if split == 0:
            lista.append(0)
        else:
            lista.append(1)
        rep -= (split * ((-2) ** cnt))
        cnt += 1
    lista.reverse()
    return''.join(map(str, lista))

print(minus_digit(N))
