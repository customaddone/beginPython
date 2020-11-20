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

N, K = 4, 4
query = [
[1, 4],
[3, 3],
[6, 2],
[8, 1]
]

# x軸, y軸を作る
x_axis = set()
y_axis = set()
for i in query:
    x_axis.add(i[0])
    y_axis.add(i[1])
x_axis = sorted(list(x_axis))
y_axis = sorted(list(y_axis))

# 経路圧縮
dp = [[0] * len(x_axis) for i in range(len(y_axis))]
for i in query:
    x = x_axis.index(i[0])
    y = y_axis.index(i[1])
    dp[y][x] += 1

dp_n = [[0] * len(x_axis) for i in range(len(y_axis))]

# 累積和
def bi_cumul_sum(dp_n, dp_bef, h, w):
    # 縦１行目、横１行目
    for i in range(h):
        dp_n[i][0] = dp_bef[i][0]
    for i in range(h):
        for j in range(1, w):
            dp_n[i][j] = dp_n[i][j - 1] + dp_bef[i][j]
    # 全て
    for i in range(1, h):
        for j in range(w):
            dp_n[i][j] += dp_n[i - 1][j]

bi_cumul_sum(dp_n, dp, len(y_axis), len(x_axis))

# 範囲内に含まれる点の数を計算する
def judge(sx, ex, sy, ey, dp):
    mother = dp[ey][ex]
    minus1 = 0
    minus2 = 0
    plus = 0
    if sx > 0:
        minus1 = dp[ey][sx - 1]
    if sy > 0:
        minus2 = dp[sy - 1][ex]
    if sx > 0 and sy > 0:
        plus = dp[sy - 1][sx - 1]
    return mother - minus1 - minus2 + plus

ans = float('inf')
for sy in range(len(y_axis)):
    for ey in range(sy, len(y_axis)):
        for sx in range(len(x_axis)):
            for ex in range(sx, len(x_axis)):
                if judge(sx, ex, sy, ey, dp_n) >= K:
                    opt = (x_axis[ex] - x_axis[sx]) * (y_axis[ey] - y_axis[sy])
                    ans = min(ans, opt)
print(ans)

# ABC151 F - Enclose All

"""
点全てを内包する円の半径の最小値は
二点間の距離の最大値　にはならない

def dis(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

N = getN()
P = [getList() for i in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dis(P[i], P[j]))

正三角形になったら当てはまらない
重心か？

3
0 0
0 1
1 0 の時重心は0.33だが実際の答えは√2/2, √2/2
二分探索したいなぁ

半径rで全てを包めるか

各点を中心に半径rの円を書く
全ての円が共有する部分があればその範囲内の1点を中心に円を書けるので
もっとrを小さくできる
"""

N = getN()
P = [getList() for i in range(N)]

def check(d):
    eps = 1 / (10 ** 10)
    points = []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            x1, y1 = P[i]
            x2, y2 = P[j]

            dif = (x1 - x2) ** 2 + (y1 - y2) ** 2
            # 半径を超えてないか
            if(dif > 4 * d ** 2):
                return False

            h = (d ** 2 - dif / 4) ** 0.5
            xm, ym = (x1 + x2) / 2, (y1 + y2) / 2

            dx,dy = (y1 - y2), -1 * (x1 - x2)
            dxy = (dx ** 2 + dy ** 2) ** 0.5

            points.append((xm + dx * h / dxy, ym + dy * h / dxy))
            points.append((xm - dx * h / dxy, ym - dy * h / dxy))

    for xp, yp in points:
        for i in range(N):
            xi, yi = P[i]
            dif = (xp - xi) ** 2 + (yp - yi) ** 2
            if(dif > d ** 2 + eps):
                break
        else:
            return True

    return False

ok = 1000
ng = 0
for _ in range(50):
    mid = (ok + ng) / 2
    if(check(mid)):
        ok = mid
    else:
        ng = mid

print(ok)
