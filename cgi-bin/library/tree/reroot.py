from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
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

# ☦️全方位木dp☦️
# https://qiita.com/Kiri8128/items/a011c90d25911bdb3ed3
class Reroot():
    def __init__(self, query):
        graph = [[] for i in range(N)]
        dist = [{} for i in range(N)]
        # 0-index
        for x, y, z in query:
            graph[x].append(y)
            graph[y].append(x)
            dist[x][y] = z
            dist[y][x] = z

        self.graph = graph
        self.dist = dist
        # トポソ
        P = [-1] * N # 親
        Q = deque([0])
        R = [] # 巡回した順番
        while Q:
            i = deque.popleft(Q)
            R.append(i)
            for a in self.graph[i]:
                if a != P[i]:
                    P[a] = i
                    # 親への辺を消す
                    self.graph[a].remove(i)
                    deque.append(Q, a)

        ##### Settings #####
        self.unit = 0 # 単位元
        self.merge = lambda a, b: max(a, b)
        self.adj_bu = lambda a, i: a + dist[i][P[i]] # マージする時の調整 iに都合のいい値を設定しよう
        # 頂点iから最も遠い点とかの場合はa + 1（子から親に行く際にエッジを一つ遡る）
        self.adj_td = lambda a, i, p: a + dist[i][P[i]]
        self.adj_fin = lambda a, i: a
        ####################
        # bottom-up
        # 頂点iからその親 piに向かうもの）
        ME = [self.unit] * N # mergeを使う
        XX = [0] * N # dpする
        for i in R[1:][::-1]: # 巡回を逆順に辿る
            XX[i] = self.adj_bu(ME[i], i) # adj_buで子要素が白である通りを追加する
            p = P[i] # 親を取り出す
            # 子要素jの持つ状態の個数 + 子要素が白である(1通り)を親要素に掛ける
            ME[p] = self.merge(ME[p], XX[i]) # iの親要素とiの値をマージする
        XX[R[0]] = self.adj_fin(ME[R[0]], R[0]) # 先頭については答えが求められるのでXXにレコード
        TD = [self.unit] * N
        for i in R: # 巡回した順番に
            ac = TD[i] # 左からDP（結果はTDに入れている）
            for j in self.graph[i]: # 各子要素について順番に更新を試みる
                TD[j] = ac # TDにはjまで累積した分が入っている
                ac = self.merge(ac, XX[j])  # マージする
            ac = self.unit # リセット 右からDP（結果はacに入れている）
            for j in self.graph[i][::-1]: # 各子要素について逆順に
                # TDに残っている左から累積した分とacにある右から累積した分をTDにマージ
                TD[j] = self.adj_td(self.merge(TD[j], ac), j, i)
                ac = self.merge(ac, XX[j]) # acの累積更新 # 逆向きにマージしていく
                # レコード 順向きのものと逆向きのものをマージする
                XX[j] = self.adj_fin(self.merge(ME[j], TD[j]), j)
        self.res = XX

# AOJ Diameter of a Tree
# 各頂点からもっとも遠い点
N = 4
query = [
[0, 1, 1],
[1, 2, 2],
[2, 3, 4]
]

tree = Reroot(query)
print(tree.res) # [7, 6, 4, 7]
