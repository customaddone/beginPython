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
A = sorted(getArray(N))
A = deque(A)
ans_list = deque([])

cnt = 0
for i in range(N // 2):

    m = A.popleft()
    if cnt % 2 == 0:
        ans_list.append(m)
    else:
        ans_list.appendleft(m)

    m = A.pop()
    if cnt % 2 == 0:
        ans_list.appendleft(m)
    else:
        ans_list.append(m)
    cnt += 1

if N % 2 == 1:
    m = A.pop()
    opt1 = abs(ans_list[0] - m)
    opt2 = abs(ans_list[-1] - m)

    if opt1 >= opt2:
        ans_list.appendleft(m)
    else:
        ans_list.append(m)

ans_list = list(ans_list)
ans = 0
for i in range(N - 1):
    ans += abs(ans_list[i + 1] - ans_list[i])
print(ans)
