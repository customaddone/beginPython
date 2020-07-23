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

N = getN()
A = [getList() for i in range(N)]
B = [getList() for i in range(N)]

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

"""
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
"""
