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
sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

class Merge():
    def __init__(self, n):
        self.n = n # グループの個数
        self.g = [set() for i in range(n)] # グループ
        self.g_name = [i for i in range(n)] # グループiの表面上の名前
        self.rev_na = [i for i in range(n)] # 表面上の名前がjのグループの真の名前は何か
        self.child = {} # どの人が何処に属するか

    # 人cがiに加入したい
    def add(self, c, i):
        if c in self.child:
            return
        # 表面上の名前i→真の名前self.rev_na[i]
        self.child[c] = self.rev_na[i]
        self.g[self.rev_na[i]].add(c)

    # 人cを退場させる
    def del(self, c):
        if not c in self.child:
            return
        self.g[self.child[c]].remove(c)
        del self.child[c]

    # uの人全員をvに移動させる
    def move(self, u, v):
        if u == v:
            return
        t_u, t_v = self.rev_na[u], self.rev_na[v]
        # 普通に移動させるだけ
        if len(t_u) <= len(t_v):
            # 所属変更
            for c in self.g[t_u]:
                self.child[c] = t_v
            # 人の移動
            self.g[t_v] |= self.g[t_u]
            # 空にする
            self.g[t_u] = set()
        # 付け替えが発生する
        else:
            # 所属変更
            for c in self.g[t_v]:
                self.child[c] = t_u
            # 人の移動
            self.g[t_u] |= self.g[t_v]
            self.g[t_v] = set()
            # 表面上の名前の交換
            self.g_name[t_u], self.g_name[t_v] = self.g_name[t_v], self.g_name[t_u]
            self.rev_na[u], self.rev_na[v] = self.rev_na[v], self.rev_na[u]

    # 人cは何処にいるか
    def where(self, c):
        return self.g_name[self.child[c]]

    # グループiにいる人は誰か
    def who(self, i):
        return self.g[self.rev_na[i]]
