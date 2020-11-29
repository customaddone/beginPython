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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# ARC060 D - 桁和

"""
n < bの時 f(b, n) = n
n >= bの時 f(b, (n // b)) + (n % b)
b, b ** 2, b *** 3で割っていく
b進数は存在するか
bはそんなに大きくなさそう
def f(b):
    n = N
    res = 0
    while n:
        res += n % b
        n //= b

    return res
でできるけど
単調増加にはならないので二分探索もできない
存在しない条件はなに
法則性なさそうなので全探索？
√nぐらいにしたい
b進数の一番上の桁は安定している

bを増やすと等間隔で数が減っていく
a(i + 1)**2 + b(i + 1) + c
ai ** 2 + 2ai + a + bi + b + c
ai ** 2 + (2a + b)i + (a + b + c)

二項
10 ** 6まで全探索
"""

N = getN()
S = getN()

def f(b):
    n = N
    res = 0
    while n:
        res += n % b
        n //= b

    return res

# 10 ** 6なので一応可能
for i in range(2, 10 ** 6 + 1):
    ans = f(i)
    if ans == S:
        print(i)
        exit()

# 10 ** 6 + 1以降について
# 割ってiになるbの最大値、最小値、そしてf(b)のとる値
for i in range(N // 10 ** 6, 0, -1):
    # 割ってiになるbの最小はN // (i + 1) + 1
    b1 = N // (i + 1) + 1
    opt1 = f(b1)
    # 割ってiになる値の最大は N // i
    b2 = N // i
    opt2 = f(b2)
    if opt2 <= S <= opt1 and (S - opt2) % i == 0:
        # 87654の場合
        # b1 = 9740 f(b1) = 10962
        # b2 = 10956 f(b2) = 14
        # opt1 - S を iで割った分をb1からひく
        print(b2 - ((S - opt2) // i))
        exit()

# 割って0になる
# これのf(b)はN
if N == S:
    print(N + 1)
    exit()

# どうもできない
print(-1)

# AGC004 B - Colorful Slimes

"""
N色のスライムがいる
全色のスライムが飼いたい
・iのスライムをaiで変色させる
・手持ちのiのスライムの全てをxで変色させる

iのスライムを入手する方法
・iのスライムをaiで購入する
・i-1のスライムをai-1で購入 + x使う
・i-2のスライムをai-2で購入 + x * 2使う...
前からやっていこう

これループする
色iのスライム買う
魔法
色iのスライム買う
魔法
で色 i+1, i+2のスライムを作れる

色iのスライム買う
魔法
魔法
色iのスライム買う
魔法
で色 i + 1, i + 3のスライムが作れる
Ai * 個数 + (iからの最長距離 * x)でいくらでもできる
各スライムについて変更した方がいいスライムについての最長距離を保持する

各スライムごとループさせる]
小さい順に？

一括に巻き込んだ方がいい場合も
4 1
4 2 3 1の場合
1を4つ買う + 魔法3回
ここまでまとめ買い変色させた方がいい境界は

魔法の回数をK回に固定すると
Ai ~ Ai-kの範囲でスライムが買える
"""

N, X = getNM()
A = getList()

mi = [float('inf')] * N
ans = float('inf')

for k in range(N): # 魔法の回数をk回に固定
    for i in range(N):
        mi[i] = min(mi[i], A[i - k])
    ans = min(ans, sum(mi) + k * X)

print(ans)

# diverta 2019 Programming Contest 2 D - Squirrel Merchant

"""
N個のどんぐり
2回する　ピッタリ整数dp

Aでは 金をga, 銀をsa, 銅をbaで交換できる
最初のAは買うだけ
Bでは 金をgb, 銀をsb, 銅をbbで交換できる
もちろん全て換金してからやる
1: 金をgb / ga倍、銀を...をする
2: 金をga / gb倍、銀を...をする

1でドングリの数が5000倍になっていることもある

O(N ** 2)で1の操作の結果のドングリの最大値はわかる 25,000,000になる
1で増やした金属は2では使わないんだから、残り最大2種類の金属を使えばいい
ga > gb, sa > sb, ba > bbの場合はドングリは5000個のまんまだから
"""

def multi(n, ga, gb, sa, sb, ba, bb):
    res = n
    for g in range(n + 1):
        for s in range(n + 1):
            # 購入金額についてオーバーしてないか
            if g * ga + s * sa > n:
                break
            b = (n - (g * ga + s * sa)) // ba
            opt = g * gb + s * sb + b * bb + (n - (g * ga + s * sa + b * ba))
            res = max(res, opt)

    return res

def multi_two(n, ga, gb, sa, sb):
    res = n
    for g in range(n + 1):
        if g * ga > n:
            break
        s = (n - (g * ga)) // sa
        opt = g * gb + s * sb + (n - (g * ga + s * sa))
        res = max(res, opt)
    return res

N = getN()
Ga, Sa, Ba = getNM()
Gb, Sb, Bb = getNM()

opt1 = multi(N, Ga, Gb, Sa, Sb, Ba, Bb)
opt2 = 0
opt3 = 0
opt4 = 0
opt5 = 0

if opt1 == N:
    # 1回目で何もしなかった場合のみ逆向きでmulti
    opt2 = multi(N, Gb, Ga, Sb, Sa, Bb, Ba)

opt3 = multi_two(opt1, Gb, Ga, Sb, Sa)
opt4 = multi_two(opt1, Gb, Ga, Bb, Ba)
opt5 = multi_two(opt1, Sb, Sa, Bb, Ba)

print(max(opt1, opt2, opt3, opt4, opt5))

#　Code Fomula 2014 予選 C - 仲良し文字列
# 間違ってるところのみ抜けば全通り試せる

def ord_chr(array, fanc):
    if fanc == 0:
        res = [ord(s) - ord('a') for s in array]
        return res

    if fanc == 1:
        res = [chr(i + ord('a')) for i in array]
        res = ''.join(res)
        return res

A = ord_chr(input(), 0)
B = ord_chr(input(), 0)

judge = [-1] * 26
psuedo = [-1, -1]
for i in range(len(A)):
    if A[i] == B[i]:
        if judge[A[i]] >= 0:
            psuedo = [judge[A[i]], i]
            break
        judge[A[i]] = i
else:
    for i in range(len(A)):
        if judge[A[i]] >= 0:
            # 1番目が埋まっていたら２番目に置く
            psuedo[(psuedo[0] != -1)] = i

opt = []
target = []

for i in range(len(A)):
    if i in psuedo or A[i] != B[i]:
        opt.append(A[i])
        target.append(B[i])

    if len(opt) > 8:
        print('NO')
        exit()

N = len(opt)

def dfs(array, time):
    if time == 3:
        if array == target:
            print('YES')
            exit()
        return

    for i in range(N):
        for j in range(i + 1, N):
            res = deepcopy(array)
            res[l], res[r] = res[r], res[l]
            dfs(res, time + 1)

dfs(opt, 0)

print('NO')

# ABC128 D - equeue

N, K = getNM()
V = getList()
m = 0

for i in range(N + 1): # 右からi個取る
    for j in range(min(K - i + 1, N - i + 1)): # 左からj個取る
        t = sorted(V[:i] + V[-j:] * (j > 0))[::-1]
        c = K - i - j # 残りc個

        while t and c and t[-1] < 0:
            t.pop()
            c -= 1
        m = max(m, sum(t))

print(m)
