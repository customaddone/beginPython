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

# CODE FESTIVAL 2016 Final D. Pair Cards

"""
個数の最大値を求める
ペア
最も条件がきついものからペアにしていく
条件　どちらか
同じ整数
Mの倍数になる
Mが奇数の場合と偶数の場合
奇数の場合
mod mが
0: 自身と
i: m - iと
偶数の場合
0, m // 2: 自身と
i: m - iと
効率のいい組み合わせ
きつい順から
min(len(i), len(m - i))になるが差分については同じ数同士をペアにできる
同じ数がグループにある数はその同じ数と結ぶことができるし、m - iのグループの数と結ぶことも
できる　条件は緩い
そうではない条件が厳しいものを優先して結ぶ
"""

N, M = getNM()
X = getList()

modulo = [[] for i in range(M)]
for x in X:
    modulo[x % M].append(x)

ans = (len(modulo[0]) // 2) + (len(modulo[M // 2]) // 2) * (M % 2 == 0)
half = M // 2 if M % 2 == 0 else (M // 2) + 1

for i in range(1, half):
    pair1 = 0
    dict1 = defaultdict(int)
    for j in modulo[i]: # 同じ数
        if dict1[j] == 1:
            dict1[j] -= 1
            pair1 += 1
        else:
            dict1[j] += 1

    pair2 = 0
    dict2 = defaultdict(int)
    for j in modulo[M - i]:
        if dict2[j] == 1:
            dict2[j] -= 1
            pair2 += 1
        else:
            dict2[j] += 1

    if len(modulo[i]) > len(modulo[M - i]): # pair1を使う
        ans += len(modulo[M - i])
        diff = abs(len(modulo[i]) - len(modulo[M - i])) // 2
        ans += min(diff, pair1)
    else:
        ans += len(modulo[i])
        diff = abs(len(modulo[i]) - len(modulo[M - i])) // 2
        ans += min(diff, pair2)

print(ans)

# AGC040 B - Two Contests

"""
数え切れないほどたくさんの人がコンテストに参加する
N問の問題がある
区間[L, R]の人は正解する　この区間は広いのでセグ木使えない
数学問か？

N問をいずれかのコンテストで出す　どちらのコンテストも１問以上出す
できるだけダブりを出す
最大の値を出す　二分探索か
貪欲っぽい
[[1, 4], [2, 5], [4, 7], [5, 8]] の時
[1, 4], [2, 5] と [4, 7], [5, 8]に分ける
[1, 4]を選択する場合、スタートが5以上になるものは選ばない
最初の一つを選ぶと上限が決まる
片方のグループは上限を見て、もう片方は下限を見る？

場合によっては片方にいらないものを押し付けることも
多分貪欲
区間スケジューリングはダブらないようにやった
[[4, 17], [3, 18], [2, 19], [1, 20]]
二分探索がしたい　だめです
上限と下限が独立ではない

１つのコンテストのmaxが一番広い幅を選んだ時
[1, 20] これに加算していってもう一つのコンテストを緩和していく

Liの最大値をとるindexをp, Riの最小値をとるindexをq
片方にいらないものを押し付ける
pとqが同じグループ もう片方は最大の幅を取るもの
pとqが違うグループ
lを昇順に並べて先頭からi個目までをqの方に
それ以外をqの方に置く
"""

N = getN()
Q = [getList() for i in range(N)]
Q.sort(reverse = True, key = lambda i:i[1])
Q.sort()

max_l = N - 1 # ソートしているので最初から出ている
min_r = 0
for i in range(N): # min_rのインデックスを探す
    if Q[i][1] <= Q[min_r][1]:
        min_r = i

# same(max_l, min_r)
dmax = 0
for i in range(N):
    if i == max_l or i == min_r: # 飛ばす
        continue
    # 最大の幅を取るものを探す
    if Q[i][1] - Q[i][0] > Q[dmax][1] - Q[dmax][0]:
        dmax = i
d1 = max(0, Q[min_r][1] - Q[max_l][0] + 1) # pとqが同じグループにある方の楽しさ
d2 = max(0, Q[dmax][1] - Q[dmax][0] + 1)
ans = d1 + d2

# !same(max_l, min_r)
# 最小のrを取る地点から順に
# それ以前はmin_rの幅より広くなるので無視して良い
min_r_list = [Q[i][1] for i in range(N)]
for i in range(N - 2, -1, -1):
    min_r_list[i] = min(min_r_list[i], min_r_list[i + 1])

q_group = [float('inf'), Q[min_r][1]]
p_group = [Q[max_l][0], 0]
# 最初が一番q_groupの幅が広い
for i in range(min_r, max_l):
    left, right = Q[i]

    q_group = [left, Q[min_r][1]] # i番目まで
    p_group = [Q[max_l][0], min_r_list[i + 1]] # i + 1番目以降
    d1 = max(0, p_group[1] - p_group[0] + 1)
    d2 = max(0, q_group[1] - q_group[0] + 1)
    ans = max(ans, d1 + d2)

print(ans)

# ABC093 D - Worst Case

"""
たくさんの人がコンテストに参加している
２回のコンテストに参加した
参加者のスコアは２つのコンテストの順位の掛け合わせ
高橋くんは１回目:A 2回目:Bだった
高橋くんよりスコアの小さい参加者（ランクが上）の最大値を求めよ

二分探索したいが
√Aであるかも
条件を満たすのは？
無駄にならないペアの作り方は貪欲でやった
該当する人の順位をa, bとすると
a < A or b < Bである必要が
a < A and b < Bにするのは明らか無駄

1  4
   3
   2
   1

b < B
b = 1の時、ペアにできるのはb = 2, 3
b = 2の時、ない

10, 5の時
aの候補[1, 2, 3, 4, 5, 6, 7, 8, 9]
bの候補[1, 2, 3, 4]

a = 1の時 b = 6 ~ 49
a = 2の時 b = 6 ~ 24
a = 3の時 b = 6 ~ 16
a = 4の時 b = 6 ~ 12
a = 5の時 b = 6 ~ 9
a = 6の時 b = 6 ~ 8 8をとる
a = 7の時 b = 6 ~ 7 7をとる
a = 8の時 b = 6 6をとる

b = 1の時 a = 11 ~ 49
b = 2の時 a = 11 ~ 24
b = 3の時 a = 11 ~ 16
b = 4の時 a = 11 ~ 12

キツイ順からペアにしていく
全部ペアが作れるので12通り
ただしA <= 10 ** 9
せめて√A
明らかに探索しなくていいものがある
cntしていくか？　鳩の巣原理
a = 8 b = 6 ok cnt += 1
a = 7 b = 6, 7 ok cnt += 1 ダメなら+= 1しない
aの数が減ってbの範囲が拡張される（されない場合もある）
ダメならcnt += 1しない
ずっと拡張されない場合がある　その場合は飛ばせるのでは
aの数が√A * Bを越えると商が1刻みになる
A = 10 B = 5の場合
a = 1 ~ 7　お気に入りの大きい数
a = 8 a = 7で7を選んだのであとは6しかない

b = 1 ~ 4　お気に入りの大きい数字
A = 1, B = 4の時
√3 = 1.7... b = 1の時は選べる
b = 2の時 bでa = 3を選んだ

すでに最大マッチングができていた場合を考える
対称性よりa, bの最大値は同じ値
aの候補
1, 2, 3... xからAを除いたもの
bの候補
1, 2, 3... xからBを除いたもの
をaの最大値とbの最大値とでマッチングさせる
a * bの最大値は中央らへんにある
a, bのどちらかがx // 2, x - (x // 2)をとる
"""

Q = getN()
query = [getList() for i in range(Q)]

def kth(m, k):
    if m >= k:
        return m + 1
    else:
        return m

def wantmax(m, A, B): #mコとった時の最大値計算(真ん中らへんを探索)
    ret = 0
    for i in range(-10, 10): # 適当に探索
        now = m // 2 + i
        if 0 < now <= m:
            ret = max(ret , kth(now, A) * kth(m - now + 1, B))

    return ret

for A, B in query:

    ok = 0
    ng = A * B

    while  ng - ok > 1:
        m = (ok + ng) // 2
        ret = wantmax(m, A, B)

        if ret >= A * B:
            ng = m
        else:
            ok = m

    print(ok)
