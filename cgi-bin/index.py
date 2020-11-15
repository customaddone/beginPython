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

# エイシング プログラミング コンテスト 2019 D - Nearest Card Game

"""
つまりnim
青木君がXiを指定する
高橋くん→青木くんの順番でAから数字を取っていく
高橋くん: 最も大きい数字を取る
青木くん: Xに最も近い数字を取る　複数あれば小さい方
カードがなくなれば終了　
各Xについて高橋くんが取るカードの合計を求めよ
O(1)でやる　テーブルで累積和とかなんかを前処理してO(1)で参照する
Nが偶数: 高橋くんはN // 2枚のカードを取る
Nが奇数: 高橋くんはN // 2 + 1枚のカードを取る

Xが変化するごとに取るカードがどのように変化するか
5 5
3 5 7 11 13
X = 1の時、近いカードは順に3, 5, 7, 11, 13
つまり高橋くんは13, 11, 7を取る
X = 4の時、近いカードは順に3, 5, 7, 11, 13
X = 9の時、近いカードは順に7, 11, 5, 13, 3
X = 10の時             11,  7,13,  5, 3

X = 10の場合　7,  5, 3...
            11, 13...
高橋くんの取るカードは    13, 11, 7,  5, 3
7と5がスキップされるので、13 + 11 + 3 = 27
高橋くん、青木くんの取る順番がわかれば得点をO(1)でもとめれればいいのだが
13, 11, 7, 5, 3
7, 11, 5, 13, 3 互いにスキップされ合う
高橋くんがiを取るスピードが青木くんより早い、もしくは同じなら取得できる
そうでなければ青木くんが取得する
X = 23の場合
高橋: 13, 11, 7, 5, 3
青木: 13, 11, 7, 5, 3
13 + 7 + 3で23 これを各O(1)で求めたいが
累積和しそうだ
NlogNまでならいける　各XiについてlogNで
青木くんが取る順番は求めなくていい？
高橋くんが取れるどうかだけ？
X = 4からの距離
1, 1, 3, 7, 9: 3 5 7 11 13
X = 5
2, 0, 2, 6, 8: 5 3 7 11 13
X = 6
3, 1, 1, 5, 7: 5 7 3 11 13
X = 7
4, 2, 0, 4, 6: 7 5 3 11 13
X = 8
5, 3, 1, 3, 5: 7 5 11 3 13
X = 9
6, 4, 2, 2, 4: 7 11 5 13 3
スワップしていく？

X = 1の時
3, 5, 7, 11, 13
X = 4の時
5, 7, 11, 13
3
X = 9の時
11, 13
7, 5, 3
Xiから近い順とA[-1]から近い順
3 5 7 11 13
     10  13
bisect_rightでXiでのスタート地点は求められる
Xi-1の時と何が違うか

A1, A3...の合計とA2, A4...の合計を求める
Aは[(高橋と青木が交互に取るゾーン), (青木が取るゾーン), (高橋が取るゾーン)]になる
その境界を求める
"""

N, Q = getNM()
A = getList()
X = getArray(Q)

csum = [0]
for i in range(N):
    csum.append(csum[-1] + A[i])
csum_even = [0]
for i in range(0, N, 2):
    csum_even.append(csum_even[-1] + A[i])
csum_odd = [0]
for i in range(1, N, 2):
    csum_odd.append(csum_odd[-1] + A[i])

#t回でX以下のAのみとなってしまうような最小のtを求める。
def calc_t(X):
    ok = -1
    ng = N + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        aoki = mid // 2
        taka = mid - aoki
        aoki_max = A[-taka]
        aoki_min_index = bisect_left(A, 2 * X - aoki_max)
        if N - taka - aoki_min_index < aoki:
            ng = mid
        else:
            ok = mid

    return ok

for x in X:
    t = calc_t(x)
    s = csum[N] - csum[N - (t + 1) // 2]

    if N % 2 == 0:
        s += csum_odd[(N - t) // 2]
    else:
        s += csum_even[(N - t + 1) // 2]
    print(s)

# CODE FESTIVAL 2015 予選A D - 壊れた電車 

"""
N両編成 M人の整備士
隣に行くのに1分かかる
全ての車両を周回するのにかかる時間は

それぞれについて境界値を求める問題
一方通行するのとジグザグに行くの２パターンある
二分探索したい k分でどこまで周回できるか
振った方が有利なのか

出来る限り右の車両を点検する
絶対にこの人にしか周回できない場所を考える
絶対に誰にもいけない左端があればout
"""

N, M = getNM()
X = getArray(M)

def judge(x):
    now = 0
    for i in range(M): # 2 ~ N番目の人について
        # now + 1番目を点検しないといけない
        # 左側にいくつ進まないといけないか
        want = max(0, X[i] - (now + 1)) # そこまで行かないといけない
        if want > x: # 時間が足りない場合False
            return False
        else:
            # 左行って右行くか、右行って左行くかどちらか大きい方
            now = max(now, X[i], X[i] + max(x - 2 * want, (x - want) // 2))

    return now >= N # 最後まで整備できたか

ok = 2 * (10 ** 9 + 7)
ng = -1 # 0回の周回でいい場合もある

while ok - ng > 1:
    mid = (ok + ng) // 2

    if judge(mid):
        ok = mid
    else:
        ng = mid

print(ok)
