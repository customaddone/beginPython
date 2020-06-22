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

def square(x1, y1, x2, y2):
    nx_1 = x1 - (y1 - y2)
    ny_1 = y1 + (x1 - x2)
    nx_2 = x2 - (y1 - y2)
    ny_2 = y2 + (x1 - x2)

    return [nx_1, ny_1, nx_2, ny_2]

N = getN()
lista = []
ans = 0
for i in range(N):
    x, y = getNM()
    lista.append((x, y))
listb = set(lista)

for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = lista[i]
        x2, y2 = lista[j]
        nx_1, ny_1, nx_2, ny_2 = square(x1, y1, x2, y2)
        if (nx_1, ny_1) in listb and (nx_2, ny_2) in listb:
            matl = (nx_1 - nx_2) ** 2 + (ny_1 - ny_2) ** 2
            ans = max(ans, matl)
print(ans)
