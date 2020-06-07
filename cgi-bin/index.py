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

X, Y = getNM()
N = getN()
query = []
for i in range(N):
    a1, b1 = getNM()
    query.append([a1, b1])
query.append(query[0])

# y = line[0]x + line[1]
# 傾きmaxならx = line[3]
def line(Ax, Ay, Bx, By):
    if Ay == By:
        return 0, Ay, None
    if Ax == Bx:
        return float("inf"), 0, Ax
    a = (Ay - By) / (Ax - Bx)
    b = Ay - a * Ax
    return a, b, None

# 点[p1, p2]を通り、傾きslopeの直線に直行する直線を求める
def perp(p1, p2, slope):
    if slope == 0:
        return float('inf'), 0, p1
    if slope > 10 ** 12:
        return 0, p2, None
    opt_slope = (1 / slope) * (-1)
    opt_inter = p2 - (opt_slope * p1)

    return opt_slope, opt_inter, None

def distance(Ax, Ay, Bx, By):
    return math.hypot(Ax - Bx, Ay - By)

# print(line(0, 2, 1, 3))
# 二つの線がクロスするx,y座標を出す
def cross(l1, l2):
    a1, b1, xx1 = min(l1, l2)
    a2, b2, xx2 = max(l1, l2)
    if a1 == a2:
        return None
    elif a2 == float("inf"):
        x = xx2
    else:
        x = (b1 - b2) / (a2 - a1)
    y = a1 * x + b1
    return x, y

x1 = query[0][0]
y1 = query[0][1]

ans = float('inf')
for i in range(1, N + 1):
    opt = 0
    x2 = query[i][0]
    y2 = query[i][1]

    # 交点を求める
    line1 = line(x1, y1, x2, y2)
    line2 = perp(X, Y, line1[0])
    cross_x, cross_y = cross(line1, line2)

    # 直線上にあるか
    range_min_x, range_max_x = min(x1, x2), max(x1, x2)
    range_min_y, range_max_y = min(y1, y2), max(y1, y2)
    if range_min_x - 10 ** 6 <= cross_x <= range_max_x + 10 ** 6 and range_min_y - 10 ** 6 <= cross_y <= range_max_y + 10 ** 6:
        opt = distance(X, Y, cross_x, cross_y)
    else:
        opt = min(distance(X, Y, x1, y1), distance(X, Y, x2, y2))

    ans = min(ans, opt)

    x1, y1 = x2, y2
    
print(ans)
