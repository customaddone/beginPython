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
mod = 998244353
MOD = 10 ** 9 + 7

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
