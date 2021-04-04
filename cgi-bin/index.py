from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
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

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# 部分和dpができる
class Bitset():
    def __init__(self, n, limit):
        # データ 初期設定は1で(0だけがある)
        self.diff = limit
        self.n = (n << self.diff)

    # 値を追加する
    def add(self, x):
        self.n |= (1 << (self.diff + x))

    # 数の配列ごとまとめて追加する
    # x > 0なら数の配列にxを足した値を追加する
    def list_add(self, d, x):
        if x >= 0:
            self.n |= (d << x)
        else:
            self.n |= (d >> -x)


    # 全ての値にxをたす 元の数は消える
    def all_add(self, x):
        if x >= 0:
            self.n = (self.n << x)
        else:
            self.n = (self.n >> -x)

    # 全ての値に足す、足さないをする
    def all_add2(self, x):
        if x >= 0:
            self.n |= (self.n << x)
        else:
            self.n |= (self.n >> -x)

    # データを引き出す　他のインスタンスに渡す用
    def data(self):
        return self.n

    # 復元用
    def res(self):
        r = []
        for i in range(self.n.bit_length()):
            if self.n & (1 << i):
                r.append(i - self.diff)
        return r

# 使い方
# ABC147 E - Balanced Path

H, W = getNM()
A = [getList() for i in range(H)]
B = [getList() for i in range(H)]

# dp[i][j][k]: i行j列の差
# -6400まで扱える
dp = [[Bitset(0, 6401) for i in range(W)] for i in range(H)]
# bitsetインスタンスに値を入れる
dp[0][0].add(B[0][0] - A[0][0])
dp[0][0].add(A[0][0] - B[0][0])

for i in range(H):
    for j in range(W):
        now = dp[i][j]
        if j < W - 1: # 右
            d = A[i][j + 1] - B[i][j + 1]
            # 現在の配列にdを足したものを次のインスタンスに渡している
            dp[i][j + 1].list_add(now.data(), d)
            dp[i][j + 1].list_add(now.data(), -d)
        if i < H - 1: # 下
            d = A[i + 1][j] - B[i + 1][j]
            dp[i + 1][j].list_add(now.data(), d)
            dp[i + 1][j].list_add(now.data(), -d)

# [-7, -6, -4, -3, -2, -1, 0, 1, 2, 3, 4, 6, 7]
print(min([abs(i) for i in dp[-1][-1].res()]))
