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

# AGC022 B - GCD Sequence

"""
Aの各要素は全て異なる
どのaiについても
gcd(ai, sum(A) - ai)が1ではない
aiとsum(A) - aiが共通因数をもつ

aiとsum(A)が共通因数を持つ

Aの全ての要素を同じ因数を持つものに変えれば簡単
全ての要素の最大公約数が1である　の場合は？
互いに素なものが１つでもあればOK

1 2 3 は条件を満たす　完全数なら話は早い　早くない　1に何してもgcdは1

N <= 10000より　1 * n, 2 * n, 3 * n...とするのは諦める
ターゲットとなるgcdの数は小さくないと間に合わない
2と3で統一してみれば
3の
3の倍数を偶数個足すと偶数になる
でも偶数と3の倍数である奇数のgcdは1
要素は3万以下であることに注意

2 ~ 30000までの偶数(15000個)
3 ~ 30000までの3の倍数かつ奇数の数(5000個) できる！！！

偶数の個数は
N % 3 == 0の時 6の倍数を先頭に
30000 + 29997, 29991
N % 3 == 1の時
2, 4 + 3, 9 逆から
N % 3 == 2の時
2, 4, 6 + 3, 9 楽

制限ないと楽だけど
限界まで2の倍数を並べればいい
N % 3 == 0　2の倍数N - 2個
N % 3 == 1  2の倍数N - 2個
N % 3 == 2  2の倍数N - 2個

N = 3の時は注意

上限を15000にすると3の個数が変動する
"""

N = getN()

def cnter(ans):
    two = 0
    three = 0
    tw_l = 0
    th_l = 0
    for i in ans:
        if i % 2 == 0:
            two += 1
            tw_l += i
        elif i % 3 == 0:
            three += 1
            th_l += i

    return tw_l % 3, th_l % 2, two, three, max(ans), min(ans)

if N == 3:
    print(2, 5, 63)
    exit()

if N % 3 == 0:
    even = min(N - 2, 15000) # 偶数の個数
    three = N - even # 基本的には2 これは偶数個でないといけない

    caution = False
    if three % 2 != 0: # even == 15000 でthreeの個数が奇数になった場合　調整1
        caution = True
        three += 1

    ans = [i * 2 for i in range(15000, 15000 - even, -1)]
    if caution: # 調整2 even -= 1
        ans.pop(0) # 30000を抜き取る

    for i in range(three):
        ans.append(i * 6 + 3)

    print(*ans)

else: # 2と3が絶対に並ぶのでgcd = 1
    even = min(N - 2, 15000) # 偶数の個数
    three = N - even

    caution = False
    if three % 2 != 0: # even == 15000 でthreeの個数が奇数になった場合　調整1
        caution = True
        three += 1

    ans = [i * 2 for i in range(1, even + 1)]
    if caution: # 調整2
        ans.pop() # 30000を抜き取る

    for i in range(three):
        ans.append(i * 6 + 3)

    print(*ans)

# Judge System Update Test Contest 202004 D - Calculating GCD

# Q個のSiについて次の問いに答えよ

N, Q = getNM()
A = getList()
S = getList()

gc = [0] * N # 最終的なXの値を求めるため
gc[0] = A[0]
# 共通因数として持っておかないといけない数が増えていく
# nowの値とA[i]に共通因数があれば残る
# 6 12 6 9 の場合は
# 2 or 3 2 or 3 2 or 3 3のみ [6, 6, 6, 3]
# gcd(S1, gc[i]) > 1なら通過 == 1なら値を出力

# gc[i]は指数関数的に減少していくんじゃ！
index = [0]
for i in range(1, N):
    gc[i] = math.gcd(gc[i - 1], A[i])
    if gc[i] < gc[i - 1]:
        index.append(i)

# gcdが変化する部分だけでgcdすればいいとわかる
# 精々2 ** 30なので30回程度
for s in S:
    for j in index:
        opt = math.gcd(s, gc[j])
        if opt == 1:
            print(j + 1)
            break
    else:
        print(math.gcd(s, gc[-1]))

# AGC026 B - rng_10s

"""
ジュースの在庫A本
B本減ります
C本以下だった場合はD本増えます
永遠にジュースを買えるか判定
各Tについて答える
数学問題か

当たり前だけどB > DならNo
A < BならNo
else
B <= CならYes
B <= D, B <= AかつB > Cの場合について（閾値が低い場合）について考える

ジュースの推移は折れ線グラフみたいになるが、
これが0を下回らないか
√Nぐらいまでならいける
Aの大きさによってはめんどくさいことになる
AをBで割ってみると
試行回数を増やすことで0に近づけることを何回もできる
0付近の動きがどうかにかかっている
9 7 5 9の場合
9 2
5以下になったので9補充 11
11 4
5以下になったので9補充 13
6 → ×
9 7 6 9 の場合だと通る
ループ検知はCが大きいので無理
AをBで引き続けるとB未満の数になる
B未満の全ての値を取りそうだが
引き続けてC以下になるとsafe
C + 1, C + 2... < Bだとout
C < i < Bとなるiを取らなければOK
BとDの倍数関係による
9 7 5 9
A + xD - yBがC + 1, C + 2...になるか　なるならout
x = 0, y = 0 9
x = 0, y = 1 2
x = 1, y = 1 11
x = 1, y = 2 4
x = 2, y = 2 13
x = 2, y = 3 6    out

互いに素ならC + 1 == Bでない限りoutになる
C + 1 < Bの場合について考える okになる場合がある
CとC + 1は少なくとも偶奇は違う　互いに素である
gcdをとる
gcdでデッドゾーンを飛び越えればOK

14 10 7 12 out 4 2
4に着地 8にも着地する out
14 10 7 11 out 4 1
14 10 8 11 out 4 1

10 10 5 10 safe 0 10
11 10 5 10 safe 1 10
1に着地　11にも着地 safe
16 10 5 10 out  6 10
10で引くと

着地点がC + 1 ~ B - 1の範囲内に入るか

A基点でmath.gcd(b, d)の部分にしか飛ばないのに気づく
"""

T = getN()
apple = [getList() for i in range(T)]

for a, b, c, d in apple:
    if b > a or b > d:
        print('No')
    else:
        if b <= c + 1:
            print('Yes')
        else:
            base = a - (a // b) * b
            split = math.gcd(b, d)
            cnt = (c + 1 - base) // split
            # 割り切れる場合 base + cnt * split = c + 1
            # 割り切れない場合 base + (cnt + 1) * split が c + 1を超える
            opt1 = base + cnt * split
            opt2 = base + (cnt + 1) * split
            # どちらかがデッドゾーンを踏んでればout
            if c + 1 <= opt1 <= b - 1 or c + 1 <= opt2 <= b - 1:
                print('No')
            else:
                print('Yes')
