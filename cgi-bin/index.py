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

# AGC005 C - Tree Restoring

"""
頂点数N Nは小さいが...
木です　
頂点1, 2... について最も遠い頂点がAi
距離iがいくつあるかcntする

最遠N - 1の距離が作れるのはパスグラフ
1 - 2 - 3 - 4 距離3が作れる
この時距離3は2つ、距離2は2つ
1 - 2 - 3
      - 4 の場合
距離2が3つ、距離1が1つ
まずパスグラフから考える
1 - 2 - 3 - 4 距離3が2つできる
              距離2は2つ
1 - 2 - 3 - 4
    　　　 - 5 距離3が3つできる

距離n - 1に一つ頂点をつなぐと距離nの頂点ができる
1 - 2 - 3
最初のパスグラフを作った時、max - 1, max - 2...の頂点が2個ずつできる
残った頂点を順番にパスグラフに刺していく

距離n - 1に一つ頂点をつなぐと距離nの頂点ができる
"""

N = getN()
A = getList()

distance = [0] * N
for i in range(N):
    distance[A[i]] += 1

opt = [0] * N # 現在距離iの頂点はいくつあるか
left = N # 残り頂点数
for i in range(N - 1, -1, -1):
    if distance[i] > 0:
        if distance[i] == 1: # 最遠は必ず2つ以上ある
            print('Impossible')
            exit()
        else:
            # 最初のパスグラフを引く
            for j in range(i + 1):
                left -= 1
                opt[max(i - j, j)] += 1
            break

# distance（クエリ）とopt(パスグラフ)を見比べる
for i in range(N - 1, 0, -1):
    # optは基礎的に存在する頂点
    # それを下回るようであればout
    if distance[i] < opt[i]:
        print('Impossible')
        exit()
    else:
        diff = distance[i] - opt[i]
        if diff: # 足さないといけない場合、距離がd - 1の頂点がなければいけない
            if opt[i - 1] == 0:
                print('Impossible')
                exit()
            else:
                left -= diff
                opt[i] += diff

if left == 0: # 頂点をちょうど使い切ったら
    print('Possible')
else:
    print('Impossible')

# ABC173 F - Intervals on Tree
# ある意味Unionfindか
# 新しい頂点を加えると、連結成分が1 - (既にある頂点へのエッジ)の分増える

"""
木の問題
N <= 10 ** 5
辺があると連結するので連結成分の個数が減る
L,RをnC2通り求める
bitは普通に間に合わない

やっぱり分解して考える
小さいのから
L = 1の時
R = 1 ~ N これにO(1)で答える
R = 1
1
R = 2 2は1と繋がってない
1
2 2
R = 3 3は1, 2と繋がっている
1 2 3 1

頂点1は何回数えられるか
頂点1が含まれるのは3回
頂点2が含まれるのは4回
頂点3が含まれるのは3回

木dpとか
前から順にやる？

Rで新しい数を入れると急に結合したりする
数え上げでしょう

ダブった部分を引く
全ての部分木の大きさを求めるのは無理そう
新しい要素は高々２つの要素を繋げるだけ

for i in range(N - 1):
    u, v = getNM()
    if u > v:
        u, v = v, u
    # 前に戻るエッジのみ
    dist[v - 1].append(u - 1)
for i in range(N):
    dist[i].sort()

ans = 0
for i in range(N): # L
    cnt = 0
    for j in range(i, N): # R
        # 範囲外に伸びるエッジは無視
        cnt += 1 - (len(dist[j]) - bisect_left(dist[j], i))
        ans += cnt

これはO(N ** 2)かかる
[[], [], [], [], [2], [], [1, 3, 4], [3], [0, 7], [5, 8]]
累積されていく
何もなければ1 ~ 10の累積で55のはず
しかし控除が累積して1 + 1 + 4(len([2] + len([1, 3, 4]))) + 5 + 7 + 9 = 27あるのでこれを引く
dist[4]の位置にある2はL = 1の時も引っかかる
dist[8]にある0は一回のみ引っかかって被害はN - 8 = 2

エッジが伸びることでいくら減るか
"""

N = getN()
dist = [[] for i in range(N)]
for i in range(N - 1):
    u, v = getNM()
    # 前に行くように
    if u > v:
        u, v = v, u
    dist[v - 1].append(u - 1)

ans = 0
cnt = 0
for i in range(N):
    ans += (i + 1) * (i + 2) // 2
    # distの探索
    for j in dist[i]:
        cnt += (j + 1) * (N - i)

print(ans - cnt)
