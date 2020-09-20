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

#############
# Main Code #
#############

class UnionFind:
    def __init__(self, N):
        """
        N:要素数
        root:各要素の親要素の番号を格納するリスト.
             ただし, root[x] < 0 ならその頂点が根で-root[x]が木の要素数.
        rank:ランク
        """
        self.N = N
        self.root = [-1] * N
        self.rank = [0] * N

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    def find(self, x):
        """頂点xの根を見つける"""
        if self.root[x] < 0:
            return x
        else:
            while self.root[x] >= 0:
                x = self.root[x]
            return x

    def union(self, x, y):
        """x,yが属する木をunion"""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        """xとyが同じグループに属するかどうか"""
        return self.find(x) == self.find(y)

    def count(self, x):
        """頂点xが属する木のサイズを返す"""
        return - self.root[self.find(x)]

    def members(self, x):
        """xが属する木の要素を列挙"""
        _root = self.find(x)
        return [i for i in range(self.N) if self.find == _root]

    def roots(self):
        """森の根を列挙"""
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_count(self):
        """連結成分の数"""
        return len(self.roots())

    def all_group_members(self):
        """{ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す"""
        return {r: self.members(r) for r in self.roots()}

N = getN()
Q = [getList() for i in range(N)]
que = deepcopy(Q)
que.sort(key = lambda i:i[1], reverse = True)
que.sort()

# xy座標が共に大きいもの
# 順列になっている？

"""
O(n**2)
U = UnionFind(N)
for i in range(N):
    for j in range(i + 1, N):
        if que[i][1] < que[j][1]:
            U.union(i, j)
for i in range(N):
    print(U.count(i))
"""
#　ソート方法はこれでOK
# やらなくていい探索がある　それを減らす
# 4 3
# 4 1
# 4 2
# 3 1
# 3 2
# 1 2 これだけいる

# 4 3 1 2でi < jになるものをペアに
# 1とペアにできるのは2, 3, 4
# 2とペアにできるのは3, 4
# 3は4
# それぞれ右側にあれば

# 6 7 5 3 2 4 1
# グループ１ 6 7
# グループ2 5
# グループ3 3 2 4
# グループ4 1
# どれか１つのグループに属する

U = UnionFind(N + 1)
group = []

for x, y in que:
    # １番目のものは必ずグループのリーダーになれる
    if not group:
        group.append(y)
        continue
    # リーダーが降順に並ぶように
    if y < group[-1]:
        group.append(y)
        continue
    opt = float('inf')
    # グループ再編成
    while group:
        # yより小さいものは全てyが所属するグループに入る
        if y > group[-1]:
            l = group.pop()
            U.union(l, y)
            opt = min(opt, l) # yが所属するグループの中のリーダー　一番最初のものが記録される
        else:
            break
    # リーダー変更
    group.append(opt)

for i in range(N):
    print(U.count(Q[i][1])) # yがiのもののサイズの大きさ　uf.funcはインデックスで呼ばなくてもいい
