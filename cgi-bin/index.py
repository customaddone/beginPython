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

# angle度のtan
def tan(angle):
    return math.tan(math.radians(angle))

# 余弦定理
A, B, H, M = 3, 4, 10, 40
minu = H * 60 + M

# 時針の角度
angh = minu / 2
# 分針の角度
angm = M * 6

# 角度の差
anglepre = abs(angh - angm)
angle = min(360 - anglepre, anglepre)

# ラジアンに直してからmath.cosとかmath.tanとか
ans = (A ** 2) + (B ** 2) - (2 * A * B * math.cos(math.radians(angle)))

# 三角形の面積4.564257194330056
print(math.sqrt(ans))

# 二つの点を通る直線の方程式を求める
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

# (1.0, 2.0, None)
p1 = line(0, 2, 1, 3)
print(p1)

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

# (-1.0, 2.0, None)
p2 = perp(0, 2, 1)
print(p2)

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

# (0.0, 2.0)
print(cross(p1, p2))

# 正方形の点を二つ入れると残りの点２つが出てくる
def square(x1, y1, x2, y2):
    nx_1 = x1 - (y1 - y2)
    ny_1 = y1 + (x1 - x2)
    nx_2 = x2 - (y1 - y2)
    ny_2 = y2 + (x1 - x2)

    return [nx_1, ny_1, nx_2, ny_2]

print(*square(1, 1, 2, 4))
