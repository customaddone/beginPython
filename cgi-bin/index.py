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

# 基本の二分探索
lista = [i for i in range(10)]

def binary_search_loop(data, target):
    imin = 0
    imax = len(data) - 1
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        if target == data[imid]:
            return imid
        elif target < data[imid]:
            imax = imid - 1
        else:
            imin = imid + 1
    return False
print(binary_search_loop(lista, 4))

# 三分探索
# ARC054 ムーアの法則
def f(x):
    return x + p / pow(2, 2 * x / 3)

p = float(input())
left, right = 0, 100

while right > left + 10 ** -10:
    # mid二つ
    mid1 = (right * 2 + left) / 3
    mid2 = (right + left * 2) / 3
    if f(mid1) >= f(mid2):
        right = mid1
    else:
        left = mid2
print(f(right))

# 三分探索整数ver
num = []
for i in range(100):
    if i < 50:
        num.append(i)
    else:
        num.append(100 - i)

left, right = 0, len(num) - 1
while abs(right - left) > 3:
    mid1 = (right * 2 + left) // 3 + 1
    mid2 = (right + left * 2) // 3
    # 最小値を求める場合は矢印逆になる
    if num[mid1] <= num[mid2]:
        right = mid1
    else:
        left = mid2
print(right)
print(left)

# ARC050 B - 花束
R, B = getNM()
x, y = getNM()
# 赤い花束をr束, 青い花束をb束とすると
# R >= xr + b
# B >= r + yb
# を満たしながらk = r + bを最大化せよ
# r = k - b
# R >= x(k - b) + b = xk - (x - 1)b
# B >= (k - b) + yb = k + (y - 1)b
# (y - 1)R >= (y - 1)xk - (x - 1)(y - 1)b
# (x - 1)B >= (x - 1)k + (x - 1)(y - 1)b
# (y - 1)R + (x - 1)B >= ((y - 1)x + (x - 1))k
# 二分探索?

def judge(k):
    # あるkを決めた時に

    # ①r >= 0, b >= 0
    # ②r + b = k
    # ③R >= xr + b = (x - 1)b
    # ④B >= r + yb = (y - 1)b
    # となるr, bが存在するか

    # R - k >= (x - 1)r
    # (R - k) / (x - 1) >= r
    # B - k >= (y - 1)b
    # (B - k) / (y - 1) >= b
    # (R - k) // (x - 1) + (B - k) // (y - 1) >= kになるか
    if R - k >= 0 and B - k >= 0 and (R - k) // (x - 1) + (B - k) // (y - 1) >= k:
        return True
    else:
        return False

ok = -1
ng = 10 ** 18 + 1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid
print(ok)

# AGC041 B - Voting Judges

"""
# 問題:N問、ジャッジ:M人
# M人のジャッジがそれぞれV問を選び、問題のスコアを１ずつあげる
# M人の投票の後、大きい方からP問が選ばれる
# 問題セットに選ばれる可能性があるのは何問あるか
M人全員が投票すれば選ばれやすくなる
選ばれるとは？
可能性がないものを数えた方が早いのでは
P番目以内にあれば無条件で通過
現在のP番目 <= A[i] + M
V <= Pなら
上からP - 1番目までのどれか + A[i]を加算させることでA[i]を強くできる　
V > Pなら？
上からP - 1番目までとA[i]を強化するとして、残りのV - P個は小さいものから順に選ぶ
A[i]を抜かせないようにしたい
A[i]より大きい数字も一緒に足される場合にはP以内に入れない
"""
N, M, V, P = getNM()
A = getList()
A.sort(reverse = True)

def judge(x):
    if x < P:
        return True
    if A[P - 1] > A[x] + M:
        return False
    # P - 1番目まで + 自身以降の数字についてはM個足す
    left = (V - (P - 1) - (N - x)) * M
    # P個目からx-1まで A[x] + Mを超えない分足す
    for i in range(P - 1, x):
        left -= A[x] + M - A[i]

    return left <= 0

ok = -1
ng = N

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid
print(ok + 1)

# ABC023 D - 射撃王
N = getN()
listh = []
lists = []
for i in range(N):
    h, s = getNM()
    listh.append(h)
    lists.append(s)
left = 0
right = 10 ** 15

for _ in range(50):
    flag = True
    mid = (left + right) // 2
    costtime = [0] * N
    for i in range(N):
        costtime[i] = (mid - listh[i]) / lists[i]
    costtime.sort()
    for i in range(N):
        if costtime[i] - i < 0:
            flag = False
    if flag:
        right = mid
    else:
        left = mid
print(right)

# ABC034 D - 食塩水

N, K = getNM()
query = [getList() for i in range(N)]

def judge(target):
    alta = []
    for i in range(N):
        salt = query[i][0] * (query[i][1] - target)
        alta.append(salt)
    alta.sort(reverse = True)
    return sum(alta[:K]) >= 0

left = -1
right = 101

for i in range(100):
    mid = left + (right - left) / 2
    if judge(mid):
        left = mid
    else:
        right = mid
print(left)

# ABC063 D - Widespread
# 最小で何回の　二分探索
# 通常攻撃time回を全員に食らわせる→爆発time回を食らわせる
# 魔物は生き残ることができるか
N, A, B = getNM()
H = getArray(N)

def judge(time, main, sub, hp):
    diff = main - sub
    cnt = 0
    for i in range(len(hp)):
        left = hp[i] - time * sub
        if left > 0:
            cnt += (left + diff - 1) // diff

    return cnt

ok = 10 ** 12 + 1
ng = -1

while ok - ng > 1:
    mid = (ok + ng) // 2
    opt = judge(mid, A, B, H)

    # mid:仮のの回数
    # opt:midを定めた時必要な爆発の回数
    # 仮の回数が必要な回数より多ければokを緩和
    if mid >= opt:
        ok = mid
    else:
        ng = mid
print(ok)

# ABC146 F - Sugoroku

# 範囲指定してエッジを引く最短路問題は大体セグ木
# seg解
# M = 3の時、1から2, 3, 4に行ける
# dp[i]: iまで行く最短の通り
# dp[i] = seg.query(i - M, i) + 1
# dpが出来上がったらdp = [1, 1, 2, inf, inf, 3, 3...]みたいなのを
# 1がある位置、2がある位置...[[0, 1], [2], [5, 6]...]としていき各子要素の一番最初の数字をとる

# 現在地点 - Mまでで最も大きく戻れる地点を探す
# 最も大きく戻っていけば最初の1 ~ i間を最小にできる
N, M = getNM()
S = input()
opt = []
for i in range(N + 1):
    if S[i] == '0':
        opt.append(i)

now = opt.pop()
ans = []
while opt:
    index = bisect_left(opt, now - M) # 現在地点 - Mまでで最も大きく戻れる地点を探す
    if index == len(opt): # なければ-1
        print(-1)
        exit()
    ans.append(now - opt[index])
    while len(opt) - 1 != index: # indexの場所まで掘る
        opt.pop()
    now = opt.pop()

print(*ans[::-1])

# エクサウィザーズ 2019 C - Snuke the Wizard

"""
各マスには文字が書かれている
各マスには１体ずつゴーレムがいる
Q回呪文を唱えゴーレムを移動させた
tが書かれたマスにいる全てのゴーレムについてd方向に移動する
右端、左端から落ちていく
盤上に残っているゴーレムの数は

antsかな？
文字の数はせいぜい26個
呪文で場所替えすると次の場所の文字に従う

3 4
ABC
A L
B L
B R
A R　の時

地点１にいてA Lされると落ちる
地点３にいてC Rされると落ちる

呪文を唱えた後の配置は求められる
求められる際tの場所にいるゴーレムしか移動しない
最終的な配置を出さなくてもいいのではないか
地点１のゴーレムに関係あるのは A L
地点２のゴーレムに関係あるのは B L, A R
地点３のゴーレムに関係あるのはない

ゴーレムがいる地点の数は減っていくんじゃ
文字sがある地点のみ探索
文字sがあり、かつゴーレムがいる地点のみholdする
10 ** 5 * 10 ** 5で無理
遅延セグ木かもしれない　

地点iにいるゴーレムが落ちるかどうか
ダブリングしたい　ダブリングではなさそう
どういう配置だとどこに行くか
地点１にいると A L すると落ちる
地点２にいると B L & A L すると落ちる
もしくは各場面で端っこに何体いるか

各文字で探索するか
配置がバラバラ

どうすれば落ちる？
A Lがある場合
Aにいる or 以前の地点でB Lがある
端っこ起点で探索
逆から見たときにA L, B L, A R...という風に並んでいると
途中でA Rがあるとキャンセル
directionをマージする

両端に墓地を置く　これらは呪文で動かない
何体のゴーレムが墓地に行かないか
あるゴーレムが左に移動するとき、もともと左にいたゴーレムを追い越すことはない
（次からは一緒に移動するため）
とするとあるゴーレムが左端から落ちるとき、それより左側にあるゴーレムも全て落ちる

二分探索が使える
単調増加/減少を見抜く
"""

N, Q = getNM()
S = input()
P = []
D = []
for i in range(Q):
    t, d = input().split()
    P.append(t)
    D.append(d)

def judge_left(p): # 左から落ちないか
    now = p
    for i in range(Q):
        if now < 0 or N <= now:
            continue
        if S[now] == P[i]:
            if D[i] == 'L':
                now -= 1
            else:
                now += 1
    return (0 <= now)

def judge_right(p): # 右から落ちないか
    now = p
    for i in range(Q):
        if now < 0 or N <= now:
            continue
        if S[now] == P[i]:
            if D[i] == 'L':
                now -= 1
            else:
                now += 1
    return (now < N)

ans = N

# judge_left
ok = 10 ** 18 + 1
ng = -1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if judge_left(mid):
        ok = mid
    else:
        ng = mid

ans -= ok

# judge_right
ok = -1
ng = 10 ** 18 + 1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if judge_right(mid):
        ok = mid
    else:
        ng = mid

ans -= (N - (ok + 1))

print(ans)
