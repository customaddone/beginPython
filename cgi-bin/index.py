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

# 基本の二分探索
lista = [i for i in range(10)]

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
print(binary_search_loop(lista, 4))

# 三分探索
# ARC054 ムーアの法則
def f(x):
    return x + p / pow(2, 2 * x / 3)

p = float(input())
left, right = 0, 100

while right > left + 10 ** -10:
    # mid二つ
    mid1 = (right * 2 + left) / 3
    mid2 = (right + left * 2) / 3
    if f(mid1) >= f(mid2):
        right = mid1
    else:
        left = mid2
print(f(right))

# 三分探索整数ver
num = []
for i in range(100):
    if i < 50:
        num.append(i)
    else:
        num.append(100 - i)

left, right = 0, len(num) - 1
while abs(right - left) > 3:
    mid1 = (right * 2 + left) // 3 + 1
    mid2 = (right + left * 2) // 3
    # 最小値を求める場合は矢印逆になる
    if num[mid1] <= num[mid2]:
        right = mid1
    else:
        left = mid2
print(right)
print(left)

# ARC050 B - 花束
R, B = getNM()
x, y = getNM()
# 赤い花束をr束, 青い花束をb束とすると
# R >= xr + b
# B >= r + yb
# を満たしながらk = r + bを最大化せよ
# r = k - b
# R >= x(k - b) + b = xk - (x - 1)b
# B >= (k - b) + yb = k + (y - 1)b
# (y - 1)R >= (y - 1)xk - (x - 1)(y - 1)b
# (x - 1)B >= (x - 1)k + (x - 1)(y - 1)b
# (y - 1)R + (x - 1)B >= ((y - 1)x + (x - 1))k
# 二分探索?

def judge(k):
    # あるkを決めた時に

    # ①r >= 0, b >= 0
    # ②r + b = k
    # ③R >= xr + b = (x - 1)b
    # ④B >= r + yb = (y - 1)b
    # となるr, bが存在するか

    # R - k >= (x - 1)r
    # (R - k) / (x - 1) >= r
    # B - k >= (y - 1)b
    # (B - k) / (y - 1) >= b
    # (R - k) // (x - 1) + (B - k) // (y - 1) >= kになるか
    if R - k >= 0 and B - k >= 0 and (R - k) // (x - 1) + (B - k) // (y - 1) >= k:
        return True
    else:
        return False

ok = -1
ng = 10 ** 18 + 1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid
print(ok)
