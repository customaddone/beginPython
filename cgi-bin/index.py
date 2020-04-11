# 便利グッズ
import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
def debug(*args):
    if debugmode:
        print(*args)
def input(): return sys.stdin.readline().strip()
def STR(): return input()
def INT(): return int(input())
def FLOAT(): return float(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
inf = sys.maxsize
mod = 10 ** 9 + 7
dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
debugmode = False

def func(now, ignore):
    # ignoreする頂点がnに達したら
    if len(ignore) == n:
        return 1
    res = 0
    for i in points[now]:
        if i in ignore:
            continue
        nignore = deepcopy(ignore)
        nignore.append(i)
        # いけるところは深さ優先で行く
        res += func(i, nignore)
    # 最後まで到達できなかったら0を返す
    return res

n, m = MAP()
ab = [LIST() for _ in range(m)]
points = [[] for _ in range(n)]
# 頂点の情報を整理
for i in range(n):
    for j in range(m):
        if ab[j][0] == i + 1:
            points[i].append(ab[j][1] - 1)
        elif ab[j][1] == i + 1:
            points[i].append(ab[j][0] - 1)
ans = func(0, [0])
print(points)
