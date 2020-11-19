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

# Mujin Programming Challenge 2017 A - Robot Racing

"""
N体のロボット
座標は全て異なり1 <= xi <= 10 ** 9 二分探索できる
dpしたいけどxが大きいのでdpできない
現在の座標から-1, -2のどちらかに進める　ダブルと他のを待たないといけない
N体のロボットがゴールする順番は何通りありますか
トポソか？
トポソの通りは求められる
どれがどれより先でないといけないかわかれば

前からdpしていくのかな
理想的な状態であればN!

ロボットiがjより先にゴールする条件
1 2 3 の場合
全部で3!
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1 ある
ただし3は1, 2より先にゴールできない
  , i, , jの場合
  , i, j,
 j, i,  ,でjはiより先に行ける

  , i, j,  の状態にできればjはiを飛び越せる
  , i, j, lの場合でも
 i,  , j, lとすればiの直後に隙間ができるので飛び越せる
できない条件は
a, b, c, i, j, lだとしても適当にa, bを動かしたら
 ,  ,  , i, j, l前に隙間ができるので動かせる
iが2番目以降にあれば後ろの駒は飛び越せそうだけど
jがiを飛び越せる→同じルートを通ってその後ろのkも飛び越せる

連なってる部分があると難しくなるみたい
トポソではなさそう

8
1 2 3 5 7 11 13 17 だと10080(8! // 4)

iが一番最初にゴールできるか
１番目にあるとできない では2番目は
1, 2, 3, , 5, 6, 7　なら
 , 2, 3, , 5, 6, 7
lim = 現在の場所 // 2個以下の駒があれば通過できる　偶数番目だとお得
前に駒がplace[i] // 2個しかなければ1位通過できる
つまり (i - (place[i] // 2)) + 1位通過できる
1, 2, 3の場合
2 1位通過はできる
3 2位通過はできる
前にある駒 - lim位通過はできる
1, 2, 3, 4位の場合
 , 2, 3, 4 4は2位通過はできる
1, 2, 3, 4, 5の場合
 , 2, 3, 4, 5 5は3位通過はできる
1: (0 - (1 // 2)) + 1 = 1
2: (1 - (2 // 2)) + 1 = 1
3: (2 - (3 // 2)) + 1 = 2
4: (3 - (4 // 2)) + 1 = 2
5: (4 - (5 // 2)) + 1 = 3

更にi番目がn番目以降でしかゴールできないなら、それより後ろのjがn - 1番目でゴールできるわけない
l[i] = max(l[i - 1], opt)
1, 2, 3, 4, 5
3が一つ遅延するので4, 5も遅延する
4に影響するのは2 2は遅延しないが4自身が遅延するのでdp[2] + 1
5は3が遅延するし5自身も遅延する
前の駒は全て1, 3, 5...と配置する
配置できない場合は+= 1
"""

N = getN()
X = getList()
l = [1] * N
now = 0
cnt = 1

for i in range(N):
    l[i] = cnt
    if X[i] < 2 * now + 1:
        cnt += 1
    else:
        now += 1

power = [0] * (N + 1)
for i in range(N):
    power[l[i]] += 1

# 最高位が決まっているときの順列の通りの求め方
ans = 1
acc = 0
for i in range(N):
    acc += power[i + 1]
    ans *= acc
    ans %= MOD
    acc -= 1

print(ans % MOD)

# ABC150 E - Change a Little Bit

"""
数列S, Tがある　これは0と1からできている xor?
Sを操作してTにする　そのコストがf(S, T)
Ciをちゃんと見る

f(S, T)の求め方からわからない
Dの数はだんだん減っていく
Cのコストが小さいものから先に処理すればいい

2
5 8 の場合は
S: 01 00 10 11 のそれぞれについてTはそれ以外
なので4 * (4 - 1) = 12
例えばS = 01 T = 10の時
1番目から先に処理 2番目は後で処理でいい
Ciの要素がn番目に小さくなる場合　とか求めるんだろ
N <= 10 ** 5 数え上げか
間違いが1つの時
間違いが２つの時
...
間違いがn個の時

間違いが1つの時
5のみ 8のみ
間違えた部分 1 0 or 0 1
合ってる部分 それぞれについて 1 1 or 0 0
2C1 * (2 ** 2) = 8

間違えが2つの時
5, 8
間違えた部分 2 ** (間違えた個数2) = 4
合ってる部分 2 ** (合ってる部分0) = 1
2C2 * (2 ** 2) = 4
それぞれの場合についてf(S, T)を求めるが
Ciの要素がd番目に大きくなる場合　とは

5
52 67 72 25 79 の時、ソート

[79, 72, 67, 52, 25]
間違えるn個を選ぶ　それぞれについて2 ** Nする

間違えが2つの時
79が1番大きくなる通りは
4C1 もう片方を決める = 4
72が1番大きくなる通りは
3C1
67が1番大きくなる通りは
2C1

79が2番目に大きくなる通りは
0C1 = 0
72が2番目に大きくなる通りは
1C1 = 1
67が2番目に大きくなる通りは
2C1 = 2

間違えが2つの時については楽に求められる

間違えが1 ~ n個の時
79が1番大きくなる通りは
間違えが1個の時　
4C0 = 1
間違えが2個の時　
4C1 = 4
間違えが3個の時
4C2 = 6
間違えが4個の時
4C3 = 4
間違えが5個の時
4C4 = 1
全部合わせると2 ** 4 = 16通り
同様に72については
2 ** (n - 1) = 8通り
67については
2 ** (n - 2) = 4通り

79が2番目に大きくなる
間違えが1個の時　
0C0 = 0
間違えが2個の時
0C1 = 0
間違えが3個の時
0C1 * 4C1 = 0...

72が2番目に大きくなる
間違えが1個
できない
間違えが2個
1C1 * 3C0 = 1
間違えが3個
1C1 * 3C1 = 3
間違えが4個
1C1 * 3C2 = 3
間違えが5個
1C1 * 3C3 = 1 2 ** (n - 1) = 8通り

72が3番目に大きくなる
できない

67が1番目
1 + 2 + 1 = 4
67が2番目
1 + 2 + 1 = 4
67が3番目
1 + 2 + 1 = 4
通りの数が同じ

5
52 67 72 25 79 の時、
全通りは2 ** 5 * (2 ** 5 - 1) = 992通りある
判定については2 ** 5 - 1 = 31通りだけ見てればいい
79は16
72は8 8
67は4 4 4
52は2 2 2 2
25は1 1 1 1 1
は？
組み合わせじゃなくbitで!!

79が一番大きい 2 ** 4 = 16
72が一番大きい 79は1固定 8通り
72が２番目に大きい 79は0固定　8通り
67が1番目に大きい 79, 72は0固定　4通り
67が2番目に大きい 2C1 * 4 = 8
67が3番目 4通り
52 1 2
2 3C1 * 2 = 6
3 3C2 * 2 = 6

79 1 * 16
72 1 1 * 8
67 1 2 1 * 4
52 1 3 3 1 * 2
25 1 4 6 4 1 * 1

足し合わせしたい
O(N)で

i時点で既にn個まで数字が出ている場合
4個目までで4個出ている

0 * nC0 + 1 * nC1 +...+n * nCn = n * 2 ** n-1になる
nCk = n / k * n-1Ck-1 より

それぞれの個数は2 ** n + n * 2 ** n-1
"""

N = getN()
C = getList()
C.sort(reverse = True)
# powだと遅い
two_table = [1]
for i in range(2 * 10 ** 5 + 7):
    two_table.append(two_table[-1] * 2)
    two_table[-1] %= mod

ans = 0
for i in range(N):
    opt = C[i]
    if i == 0:
        # powの第2引数にマイナスを使えない
        opt *= (two_table[i] + i * two_table[0]) % mod
    else:
        opt *= (two_table[i] + i * two_table[i - 1]) % mod
    opt %= mod
    opt *= two_table[N - i - 1]
    opt %= mod

    ans += opt
    ans %= mod

ans *= two_table[N]
print(ans % mod)
