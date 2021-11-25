
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

# 0-index サイズ気持ち大きめで建てて
class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1

    def add(self, a, w):
        x = a + 1
        while(x <= self.N):
            self.bit[x] += w
            x += x & -x

    def get(self, a):
        ret, x = 0, a
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    def cum(self, l, r):
        return self.get(r) - self.get(l)

    # xより左にあるフラグのうちもっとも右にあるフラグを探す
    # bit.get(x)そもそも左にフラグがあるか　なければlowerboundは0を示すが0にフラグはない
    # bit.lowerbound(bit.get(x)) 探す
    # bit.lowerbound(bit.get(x) + 1) 自身あるいは自身より右位にあるフラグのうち一番左にあるものを探す
    def lowerbound(self,w):
        if w <= 0:
            return 0
        x = 0
        k = self.b
        while k > 0:
            if x + k <= self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x

# 二分探索木もどき
# binary search tree
class BST:
    # arrayでどんな値が来るか読み込ませる
    # arrayはソートした配列をいれてね
    def __init__(self, N, array):
        self.N = N
        self.bit = [0] * (N + 2)
        self.comp = {} # value → index
        self.rev = {} # index → value
        for i, a in enumerate(array + [float('inf')]):
            self.comp[a] = i + 1
            self.rev[i + 1] = a
        self.b = 1 << N.bit_length() - 1

    # rev[a]以下の数字の個数を数える
    def get(self, a):
        ret, x = 0, a - 1
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    # 追加 1-indexで収納される
    def add(self, a):
        x = self.comp[a]
        while(x <= self.N):
            self.bit[x] += 1
            x += x & -x

    # 削除
    def erase(self, a):
        x = self.comp[a]
        while(x <= self.N):
            self.bit[x] += -1
            x += x & -x

    # xより大きい最小の値を返す
    def up_min(self, x):
        # self.get(self.comp[x])でx以上の値のうち最小のもの
        # self.get(self.comp[x] + 1)でxより大きい最小の値を返す
        now = self.get(self.comp[x])
        ind = self.lowerbound(now + 1)
        return self.rev[ind]

    # x番目の値を返す
    def query(self, x):
        ind = self.lowerbound(x)
        return self.rev[ind]

# 座圧BIT 0-index
class Comp_BIT:
    def __init__(self, N, array):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1
        # 座圧 1-indexで
        s = set(array)
        s = sorted(list(s))
        self.alter = {}
        self.rev = {}
        for i in range(len(s)):
            self.alter[s[i]] = i + 1
            self.rev[i + 1] = s[i]

    def add(self, a, w):
        x = self.alter[a]
        while(x <= self.N):
            self.bit[x] += w
            x += x & -x

    # [0, a)の合計
    def get(self, a):
        ret, x = 0, self.alter[a] - 1
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    # [0, a]（閉区間）の合計
    def get_rig(self, a):
        ret, x = 0, self.alter[a]
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    # [l, r)の合計
    def cum(self, l, r):
        return self.get(r) - self.get(l)

    # 小さい方からx番目の数字を探す
    def lowerbound(self, w):
        if w <= 0:
            return 0
        x = 0
        k = self.b
        while k > 0:
            if x + k <= self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return self.rev[x + 1]

# ARC033 C - データ構造
# 座圧BIT
Q = getN()
que = [getList() for i in range(Q)]

# データに入れる数字を抽出する
A = []
for t, x in que:
    if t == 1:
        A.append(x)

bit = Comp_BIT(Q + 1, A)
for t, x in que:
    if t == 1:
        bit.add(x, 1)
    else:
        # 小さい方からx番目の数字を探す
        opt = bit.lowerbound(x)
        print(opt)
        bit.add(opt, -1)

# 転倒数がK以下の連続部分列 + 通常のBITを使う方法(0-indexになる)

"""
[0, a)までの転倒数　求められる
[1, a)の転倒数は？
0番目の数字について、a)までの数字の中で自分より小さい数字の個数を引く
bit = BIT(N + 1)
cnt = 0
for i in range(1, N + 1):
    cnt += i - 1 - bit.get(A[i] + 1)
    bit.add(A[i], 1)
    print(cnt)

左位置をずらしていく
区間[l, r]の転倒数 =
Σr=0 r - l - 区間内の自身より左にある自身以下の数(i - l - bit.get_rig(A[i])) =
Σl=0 区間内の自身より右にある自身未満の数(bit.get(A[l]))

BITについて
転倒数がK以下の連続部分列については尺取り法でやることが可能
lを動かす都度A[l]を消去していく
"""

N, K = getNM()
A = getList()

bit = Comp_BIT(N + 1, A)
bit_cnt = Comp_BIT(N + 2, [i for i in range(N + 2)]) # 通常のBIT
bit_cnt.add(0, 1) # 0-indexで使う

inv = 0 # 転倒数
l = 0 # 左端（最大）

for i in range(N):
    # 今まで置いた数 - 自身より左にある自身以下の数
    inv += i - l - bit.get_rig(A[i])
    bit.add(A[i], 1)
    # invがK以下になるまでlをずらす　尺取り法
    # 自身より右にある自身より小さい数を引く
    while inv > K:
        inv -= bit.get(A[l])
        bit.add(A[l], -1)
        l += 1
    # [l, i + 1)の値をi + 1に登録
    bit_cnt.add(i + 1, bit_cnt.cum(l, i + 1) % mod)

# bit_cntのi + 1の値を求める
print(bit_cnt.cum(i + 1, i + 2) % mod)

# 区間加算bit
# ARC068 E - Snuke Line
N, M = 3, 3
P = [[1, 2, 2], [2, 3, 2], [3, 3, 1]]
P.sort(key = lambda i:i[2], reverse = True)

#### 区間加算bit ################################
bit1 = BIT(M)
bit2 = BIT(M)
# [l, r)にxを加算する
def range_add(l, r, x):
    bit1.add(l, x)
    bit1.add(r, -x)
    bit2.add(l, (-1) * x * (l - 1))
    bit2.add(r, x * (r - 1))
# [1 ~ a)までの値を集計する
def range_get(a):
    return bit2.get(a) + (a - 1) * bit1.get(a)
################################################

# 1-indexにしてある
for m in range(1, M + 1):
    # 区間の長さがmより小さいものについて取り出す
    while P and P[-1][2] <= m:
        l, r, _ = P.pop()
        range_add(l, r + 1, 1) # [l, r + 1)について区間加算
    ans = len(P)
    # 各倍数について土産の数を調べる　互いにダブらない
    for i in range(m, M + 1, m):
        ans += range_get(i + 1) - range_get(i)
    print(ans)
