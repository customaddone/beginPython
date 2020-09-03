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

# https://www.slideshare.net/drken1215/ss-86894312
N = 3
K = 4
que = [
[1, 1],
[1, 3],
[2, 2],
[3, 2]
]

# 始点を0、縦座標rowを1 ~ N, 横座標colをN + 1 ~ 2N, 終点を2N + 1にする
# 1-indexならこれでいい
# 二分グラフの最小点被覆は最大マッチング
# 二分グラフの最大安定集合は上記を除く補集合
dist = []
for i in range(1, N + 1): # 始点、終点
    dist.append([0, i, 1])
    dist.append([i + N, 2 * N + 1, 1])
for a, b in que: # 各惑星について
    dist.append([a, b + N, 1])

N = 2 * N + 2 # 2 * N + 2倍に拡張する
lines = defaultdict(set)
cost = [[0] * N for i in range(N)]
for i in range(len(dist)):
    a, b, c = dist[i]
    lines[a].add(b)
    cost[a][b] += c
print(dist)
ans = 0

# 二部マッチング問題なので最大流
# staからスタート
def Ford_Fulkerson(sta, end):
    global ans
    queue = deque()
    queue.append([sta, float('inf')])

    ignore = [1] * N
    ignore[sta] = 0

    route = [0] * N
    route[sta] = -1

    while queue:
        s, flow = queue.pop()
        for t in lines[s]:  #s->t
            if ignore[t]: #未到達
                # flowは入ってくる量、出る量のうち小さい方
                flow = min(cost[s][t], flow)
                route[t] = s
                queue.append([t, flow])
                ignore[t] = 0
                if t == end: #ゴール到達
                    ans += flow
                    break
        else:
            continue #breakされなければWhile節の先頭に戻る
        # Falseはされない
        break
    else:
        return False

    t = end
    s = route[t]
    # goalまで流れた量はflow
    # 逆向きの辺を貼る
    while s != -1:
        #s->tのコスト減少，ゼロになるなら辺を削除
        cost[s][t] -= flow
        if cost[s][t] == 0:
            lines[s].remove(t)
            #t->s(逆順)のコスト増加，元がゼロなら辺を作成
        if cost[t][s] == 0:
            lines[t].add(s)

        cost[t][s] += flow

        # 一つ上の辺をたどる
        t = s
        s = route[t]

    return True

while True:
    # ちょびちょび流して行ってゴールまで流れなくなったら終了
    if Ford_Fulkerson(0, N - 1):
        continue
    else:
        break

print(ans)
