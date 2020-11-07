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

#############
# Main Code #
#############

# 第一回日本最強プログラマー学生選手権-予選- C - Cell Inversion

"""
２N個のますがある
N <= 10 ** 5
各マスの色はBかW
異なる2マスを選んでその区間を反転させる
ちょうどN回行う　全てのマスを１回ずつ
全てのマスを白色にする通りは comboかdp

dpだとすれば前からdpしていく
全てのマスを白色

2
BWWB だとすると　1, 3 + 2, 4と2, 4 + 1, 3は同じ通り
つまり条件を満たす数字の組みをN個選んでfactorial 順番は関係ない
Wなら選ばれた累積が偶数回、Bなら奇数回あればいい
1と対応するマスは、2と対応するマスは...
S[i]が選ばれた回数が奇数回、偶数回でdpとると
同じところは２回選ばれないのでどうすれば

セグ木使う？
通りを求めるのである
1, 2の時
選べるのは3, 4のみ ×
1, 3の時
選べるのは2, 4のみ ×
一つ選ぶと次からの通りが結構制限させる

一つ選ぶとスケールを縮小した部分問題になるか？
区間を選ぶのを始点、終点の２つで分解してみると？
[i, j]を選ぶとは
0 ~ i - 1, j + 1 ~ Nまでは反転しない
[i, j]だけ反転する
2 2 2 1 1 1 2 2
1, 3, 2, 4の場合は
1 1 1
1 1 1 1
1 1 1 1
  1 1 1
 [i, j]を選ぶと
まず全体が+1され、
0 ~ iが+1され
j ~ Nが+1される
地点tについて
0 ~ tを加算するかt ~ Nを加算するか

地点tがBなら
0 ~ t - 1について右側加算を選ぶ個数 + t + 1 ~ Nについて左側加算を選ぶ回数が
奇数個でなければならない

右側加算するもの、左側加算するものを選ぶ
iについて右側加算したケース、左側加算したケース
全て右側加算とかはできない
全通りだとO(N ** 2)
多分dpなんだよなぁ
1, 3 + 2, 4と1, 4と2, 3は同じ効果
どれを右側加算にし、どれを左側加算にするか
R R R L L L

[R, L]のピースを2Nのマスの中に適当に入れる
1番目について影響があるのは[1, i]のピースのみ
1番目は自力でWにしないといけない
1はBでないといけない　B,Wだと制限がある
絶対に[1, i]のピースがあるので、デフォルトで全てに+1される
2番目[1, 2]があった場合以外は2はWでないといけない[2, i]が存在するため

区間に入るとは？
0 ~ t - 1にRが t + 1 ~ NにLが存在すること

通りの数は
NC2 * N-2C2 *...
1番目[1, i]を選ぶ
2番目

Lを選ぶとi - 1番目とi番目の色の関係が変化
Rを選ぶとi番目とi + 1番目の色の関係が変化
diを左側として選ぶならL,右側として選ぶならRとする
Si-1 = Siなら di-1 != di
Si-1 != Siなら di-1 = di

反転問題は境界で左右の要素の状態が変わると捉える
"""

N = getN()
S = input()
MOD = 10 ** 9 + 7

LR = []
d = 0
# diに何を置くか、LとRの数は一致しているかを調べる
for s in S:
    if s == 'B':
        if d % 2:
            LR.append('R')
            d -= 1
        else:
            LR.append('L')
            d += 1
    else:
        if d % 2:
            LR.append('L')
            d += 1
        else:
            LR.append('R')
            d -= 1
    if d < 0:
        print(0)
        exit()
if not d == 0:
    print(0)
    exit()

ans = 1
d = 0
# 数字の組み合わせの通りを求める
for m in LR:
    if m == 'L':
        d += 1
    else:
        # Rが出たら既に出たLを一つペアにし、消す
        ans *= d
        ans %= MOD
        d -= 1

# 組みの個数はN個あるがそれをN!する
for i in range(N):
    ans *= (i+1)
    ans %= MOD
print(ans)
