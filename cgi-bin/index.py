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

#####segfunc#####
def segfunc(x, y):
    return x + y
#################
#####ide_ele#####
ide_ele = 0
#################
class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

"""
チェックポイントごとの掛け算にならないか
x1+y1Cx1 * x2+y2Cx2...
セグ木?
0 ~ 1 seg(0, 1)
1 ~ 2 seg(1, 2)...
i番目のチェックポイントが変更されると
seg.update(i)とseg.update(i + 1)する
組み合わせの数が大きい　どうやって状態を持つか
因数を持つとか
10 * 9 * 8 と3 * 2 * 1を持つ

分子の方はx!で共通している
分母の状態を持てばいいr!(n - r)!
rと(n - r)でそれぞれセグ木
対数を持つか　足し算引き算になる
x2-x1 + y2-y1
i番目を変更
"""

N = getN()
P = [getList() for i in range(N)]
Q = getN()
que = [getList() for i in range(Q)]

# combo数を対数化して返す
table = [0] * (2 * 10 ** 6 + 7)
for i in range(2, 2 * 10 ** 6 + 7):
    table[i] = math.log2(i) + table[i - 1]

def comb(p1, p2):
    x = abs(p1[0] - p2[0])
    y = abs(p1[1] - p2[1])
    # x+y! / x!y!
    return table[x + y] - table[x] - table[y]

seg = SegTree([0] * N, segfunc, ide_ele)
for i in range(N - 1):
    # seg(i): i ~ i + 1のcombo数
    seg.update(i, comb(P[i], P[i + 1]))

for q in que:
    # 更新
    # 前のやつと今のやつが変更
    if q[0] == 1:
        t, k, a, b = q
        k -= 1
        P[k] = [a, b]
        # 前のやつ
        if k > 0:
            seg.update(k - 1, comb(P[k - 1], P[k]))
        # 今のやつ
        if k < N - 1:
            seg.update(k, comb(P[k], P[k + 1]))
    else:
        t, f1, f2, s1, s2 = q
        if seg.query(f1 - 1, f2 - 1) > seg.query(s1 - 1, s2 - 1):
            print('FIRST')
        else:
            print('SECOND')
