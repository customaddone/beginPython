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
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

#####segfunc#####
def segfunc(x, y):
    return min(x, y)
#################

#####ide_ele#####
ide_ele = float('inf')
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

# 区間を3つに分ける
# max(区間1) = min(区間2) = max(区間3
# 真ん中から求めて行った方が楽そう
# 小さい順に置いていく　真ん中の区間はそれしか選んではいけない　全ての連続部分和は探索できない

# 左から順に求めると？　中、右をlogNで求められるか　max(left)の値だけ置いていく　それしか選べない
# 中の右端からいくつ選べるかはわかる　max(right)が同じになるやつと接続できれば
# ma_lの値は単調増加
# xがある地点とx以上がある領域(だんだん増えていく)を抑えないといけない
# 尺取り法をする
# iが進むma_lが増える　中ブロックの範囲が狭まる
# 範囲内のxがあるポイントとma_r[j] = xのポイントを探す

N = getN()
A = getList()
ma_l = deepcopy(A)
ma_r = deepcopy(A)
for i in range(1, N):
    ma_l[i] = max(ma_l[i], ma_l[i - 1])
    ma_r[-i-1] = max(ma_r[-i-1], ma_r[-i])
seg = SegTree(A, segfunc, ide_ele)

# ma_l[i]以下の領域
for i in range(N - 1):
    # 領域は存在しない
    if ma_l[i] > A[i + 1]:
        continue
    # セグ木で二分探索 x以上の領域が続く範囲を探索
    ok, ng = i + 1, N
    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if seg.query(i + 1, mid + 1) >= ma_l[i]:
            ok = mid
        else:
            ng = mid
    print(i + 1, ok, ng)
