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
from math import sqrt
from fractions import gcd
import random
import string
import copy
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

def binary_search_loop(data, target):
    imin = 0
    imax = len(data) - 1
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        if target == data[imid]:
            return imid
        elif target < data[imid]:
            imax = imid - 1
        else:
            imin = imid + 1
    return False

N = 6
A = [-45, -41, -36, -36, 26, -32]
B = [22, -27, 53, 30, -38, -54]
C = [42, 56, -37, 75, -10, -6]
D = [-16, 30, 77, -46, 62, 45]

re_A = []
re_C = []
for i in range(N):
    for j in range(N):
        re_A.append(A[i] + B[j])
re_A.sort()

for i in range(N):
    for j in range(N):
        re_C.append(C[i] + D[j])
re_C.sort()

ans = 0
for i in re_A:
    # 該当する数字があった場合の左端
    ind1 = bisect_left(re_C, 0 - i)
    # 右端
    ind2 = bisect_left(re_C, 0 - i + 1)
    ans += ind2 - ind1
print(ans)
