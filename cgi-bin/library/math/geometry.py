from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

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

# 回転行列
# vec = [[x, y]]
# vecをang(ラジアンで)だけ回転してくれる
vec = [[1, -2]]
def rotate(vec, ang):
    rot = [[math.cos(ang), -math.sin(ang)], [math.sin(ang), math.cos(ang)]]
    # 行列累乗して返す(matrix.pyに置いてある)
    return array_cnt(vec, rot)

r = rotate(vec, -math.pi * 2 / N)

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

# 点が２つだと面積ができない
if N == 2:
    print(((B[1][0] - B[0][0]) ** 2 + (B[1][1] - B[0][1]) ** 2) ** .5 / ((A[1][0] - A[0][0]) ** 2 + (A[1][1] - A[0][1]) ** 2) ** .5)
    exit()

def getG(XY):
    n = len(XY)
    total_x, total_y = 0, 0
    for x,y in XY:
        total_x += x
        total_y += y
    return (total_x/n, total_y/n)

def getD(XY, Gx, Gy):
    ret = 0
    for x,y in XY:
        d = ((x - Gx) ** 2 + (y - Gy) ** 2) ** .5
        ret = max(ret, d)
    return ret

# 重心 : G
GAx, GAy = getG(A)
GBx, GBy = getG(B)

# 重心から最も遠い点までの距離 : D
DA = getD(A, GAx, GAy)
DB = getD(B, GBx, GBy)

# 拡大比率
ans = DB / DA
print(ans)

# 凸包
def area(X, Y, Z):  # 三角形の符号付き面積の2倍
    return (Y[0] - X[0]) * (Z[1] - X[1]) - (Y[1] - X[1]) * (Z[0] - X[0])

def ConvexHull(A):  # Aの凸包を形成する点のリストを返す
    A = sorted(A, key = itemgetter(0,1))  # 適宜変更
    res = []
    N = len(A)
    for i in range(N):  # 下側
        a = A[i]
        while len(res) > 1 and area(res[-2], res[-1], a) <= 0:  # 適宜'>,<,>='に変更
            res.pop()
        res.append(a)
    r = len(res)
    for i in range(N - 2, -1, -1):  # 上側
        a = A[i]
        while len(res) > r and area(res[-2], res[-1], a) <= 0:  # 適宜'>,<,>='に変更
            res.pop()
        res.append(a)
    return res

def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# キャリパー法(Rotating Calipers法)
# 凸多角形を回転しながら走査し、最遠点対を求める
def rotating_calipers(ps):
    qs = ConvexHull(ps)
    n = len(qs)

    if n == 2:
        return dist(qs[0], qs[1])

    i = j = 0

    for k in range(n):
        if qs[k] < qs[i]: i = k
        if qs[j] < qs[k]: j = k

    res = 0
    si = i
    sj = j
    while i != sj or j != si:
        res = max(res, dist(qs[i], qs[j]))
        if area(qs[j], qs[i - n + 1], qs[j - n + 1]) < 0:
            i = (i + 1) % n
        else:
            j = (j + 1) % n
    return res

A.sort()
B.sort()
a_d = rotating_calipers(A)
b_d = rotating_calipers(B)
print(b_d / a_d)

# グラハムスキャン(2次元の場合使用可能)

# 凸包の面積比の平方根
# 凸包を形成する各頂点が出る
C = ConvexHull(A)
D = ConvexHull(B)
SC = 0
SD = 0
for i in range(len(C) - 2):
    SC += area(C[0], C[i + 1], C[i + 2])
    SD += area(D[0], D[i + 1], D[i + 2])

print((SD / SC) ** .5)

# ユークリッド距離を求める
def euc(px1, py1, px2, py2):
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2)

# ２円の交点を求める
# 交点がない場合は使えないよ
def cross(x1, y1, x2, y2, r1, r2):

    # cosθを求める
    d = euc(x1, y1, x2, y2)
    cos = (r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d)
    # |P1H|
    d1 = r1 * cos

    # |AH|
    d3 = math.sqrt(r1 ** 2 - d1 ** 2)
    # P1 ~ Hのベクトル
    e = (x2 - x1, y2 - y1)
    e1 = (e[0] * d1 / d, e[1] * d1 / d)
    # A ~ Hのベクトル
    # eを90度回転させたものにd3 / dをかける
    e2u, e2d = ((e[1] * (-1)) * d3 / d, e[0] * d3 / d), (e[1] * d3 / d, (e[0] * (-1)) * d3 / d)

    return (x1 + e1[0] + e2u[0], y1 + e1[1] + e2u[1]), (x1 + e1[0] + e2d[0], y1 + e1[1] + e2d[1])
