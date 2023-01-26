
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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

num = [2, 4, 6, 8]
limit = 10

def part_bitset1(num, limit):
    N = len(num)
    dp = 1 # 最初の0

    for i in range(N):
        dp |= (dp << num[i])

    return bin(dp)

max_diff = 30

def part_bitset2(num, limit):
    N = len(num)
    dp = 1 << max_diff # 最初の0
    print(bin(dp))

    for i in range(N):
        # +, -を加える
        dp |= (dp << num[i]) | (dp >> num[i])

    return dp

l = part_bitset2(num, limit)
# 復元
ans = []
for i in range(l.bit_length()):
    if l & (1 << i):
        ans.append(i - max_diff)
# [-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(ans)

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
            # self.n = (self.n << x) | (self.n >> x)
        else:
            self.n = (self.n >> -x)
            # self.n = (self.n >> -x) | (self.n << -x)

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

# ビットセットライブラリ
class Bitset:
    '''
        N:       bitの長さ
        add():   xビット目を1にする
        sub():   xビット目を0にする
        count(): 1となるビットの数を取得
        self[x]: xビット目を取得
        bit演算子 &, | 対応
    '''
    def __init__(self, N):
        self.bit_size = 63
        self.bits_size = (N + self.bit_size - 1) // self.bit_size
        self.bits = self.bits_size * [0]
        self.N = N

    def add(self, x):
        self.bits[x // self.bit_size] |= 1 << (x % self.bit_size)

    def sub(self, x):
        self.bits[x // self.bit_size] &= ~(1 << (x % self.bit_size))

    def count(self):
        cnt = 0
        for x in self.bits:
            c = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)
            c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
            c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
            c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
            c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
            c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
            cnt += c

        return cnt

    def __and__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] & other.bits[i]

        return _bitset

    def __or__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] | other.bits[i]

        return _bitset

    def __xor__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] ^ other.bits[i]

        return _bitset

    def __getitem__(self, x):
        return self.bits[x // self.bit_size] >> (x % self.bit_size) & 1

# ABC258 G - Triangle
N = getN()
bi = [Bitset(N) for i in range(N)]
for i in range(N):
    s = input()
    for j in range(i + 1, N):
        if s[j] == '1':
            bi[i].add(j)

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        if bi[i][j] == 1:
            ans += (bi[i] & bi[j]).count()
print(ans)
