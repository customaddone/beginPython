from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
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

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(1000000)
INF = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# ここの設定を変えて使う
#####segfunc#####
def segfunc(x, y):
    return max(x, y)
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

N = getN()
A = getList()

# O(NlogN)
def lis_len(ar):
    n = len(ar)
    seg = SegTree([0] * (n + 1), segfunc, ide_ele)
    res = [0] * n
    for i in range(n):
        # j < i and A[j] < A[i]となるA[j]の最大値 + 1
        val = seg.query(0, ar[i])
        res[i] = val + 1
        seg.update(ar[i], max(seg.query(ar[i], ar[i] + 1), val + 1))
    return res

opt_a = lis_len(A) # 前からlisした時
opt_b = lis_len(A[::-1])[::-1] # 後ろからlisしたとき

ans = 0
for a, b in zip(opt_a, opt_b):
    ans = max(ans, a + b - 1)

print(ans)
