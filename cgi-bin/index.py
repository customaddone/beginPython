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

N1 = 3
dist1 = [
[1, 2],
[0, 2],
[0, 1]
]

N2 = 4
dist2 = [
[1, 3],
[0, 2],
[1, 3],
[0, 2]
]

color1 = [-1] * N1
color2 = [-1] * N2

pos = deque([0])

def colored(N, dist, color):
    pos = deque([0])
    color[0] = 0
    while len(pos) > 0:
        now = pos.popleft()

        for i in dist[now]:
            if color[i] >= 0:
                continue

            lista = set()
            for l in dist[i]:
                lista.add(color[l])

            for j in range(N):
                if not j in lista:
                    color[i] = j
                    break

            pos.append(i)

    return color

print(colored(N, dist2, color2))
