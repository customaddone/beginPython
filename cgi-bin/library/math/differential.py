from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
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

def solv_quadratic_equation(a, b, c):
    """ 2次方程式を解く  """
    D = (b ** 2 - 4 * a * c) ** (1 / 2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)

    return x_1, x_2

def is_integer_num(n):
    if isinstance(n, int):
        return n
    if isinstance(n, float):
        if n.is_integer():
            return int(n)
    return False

# 積分したい

# 正の整数x, yについて、y <= n / x を満たす点(x,y)の個数（積分）を返したい
# x = i(1 <= i <= n)としたとき、対応するyの最大値は何かを返す関数を作る
# N = 10の時
# x = [1, 2, 3, 5, 10], y = [10, 5, 3, 2, 1]
# xが6 ~ 10をとる時、yが1をとる
# xが4 ~ 5をとる時、yが2をとる
# xが3をとる時、yが3をとる
# xが2をとる時、yが2をとる
# (x[i] - x[i - 1]) * yの総和が積分になる
def integral(n):
    # n/xを微分すると-n/x^2になる
    # -n/x^2 <= 1: i <= √n である間は一つのyにつき対応するxは1もしくは複数ある
    res_x = deque([])
    res_y = deque([])
    limit = math.sqrt(n) # f(x)' = 1になるxを求める
    now = n
    for i in range(1, int(limit) + 1):
        res_x.appendleft(n // i)
        res_y.appendleft(i)

    # i > √nになる部分については一つのyにつき対応するxは0か1なので
    # 今度はxに対応するyを求める
    for i in range(res_x[0] - 1, 0, -1):
        res_x.appendleft(i)
        res_y.appendleft(n // i)
    return list(res_x), list(res_y)

print(integral(10))
