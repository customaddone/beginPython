from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
# sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# ARC068 E - Snuke Line

"""
約数により単調減少していきそう
愚直にやると
各Mにつき倍数のとこに置いていく MlogM
各MにつきNでいくつ取れるかを見る NM

二分探索とかしたいが
各おみあげについてMが幾つの時に獲得できるか　セグメントツリーでできるか
この区間に幾つの因数が入っているか
l, rが全区間　これがM個ある時対応できない
個数だけを見ていく方針で　包除原理とか

素数のところだけを数えることはできる　合成数のはどうする？

一定間隔dで移動する時
土産の幅がdより大きい場合は一回以上訪れる
土産の幅がd以下の場合は最大でも1回だけ訪れる

dより大きい幅の場合は単純に計算できる
dより大きい幅について
各点でいくつ土産の種類があるかを数え、dの倍数について数える
最大でも1回だけ訪れる土産しかないのでダブることはない

ダブらないように数えるのがミソ

N, M = getNM()
P = [getList() for i in range(N)]
P.sort(reverse = True)

for m in range(1, M + 1):
    p = [i for i in P if i[1] - i[0] + 1 <= m]
    l = [0] * (M + 1)
    q = []
    ans = N - len(p) # 一回以上訪れる
    # 各倍数について調べる
    for i in range(m, M + 1, m):
        while p and p[-1][0] <= i:
            heappush(q, p.pop()[1])
        while q and q[0] < i:
            heappop(q)
        ans += len(q)
    print(ans)

これで答えが出るがこのままだとTLE
pに集計されるPの要素の数はだんだんと増えていく
mについて調べる
区間の長さがmのものを取り出し、区間[l, r]に区間加算
mの倍数について調べる
"""

N, M = getNM()
P = []
for _ in range(N):
    l, r = getNM()
    P.append([l, r, r - l + 1])
P.sort(key = lambda i:i[2], reverse = True)

#### 区間加算bit ################################
bit1 = BIT(M)
bit2 = BIT(M)
# [l, r)にxを加算する
def range_add(l, r, x):
    bit1.add(l, x)
    bit1.add(r, -x)
    bit2.add(l, (-1) * x * (l - 1))
    bit2.add(r, x * (r - 1))
# [1 ~ a)までの値を集計する
def range_get(a):
    return bit2.get(a) + (a - 1) * bit1.get(a)
################################################

# 1-indexにしてある
for m in range(1, M + 1):
    # 区間の長さがmより小さいものについて取り出す
    while P and P[-1][2] <= m:
        l, r, _ = P.pop()
        range_add(l, r + 1, 1) # [l, r + 1)について区間加算
    ans = len(P)
    # 各倍数について土産の数を調べる　互いにダブらない
    for i in range(m, M + 1, m):
        ans += range_get(i + 1) - range_get(i)
    print(ans)

# codeforces # 635 D-MEX maximizing
# １個ずつ足していく場合のAの中の最小値とその最小値の場所を探す

"""
yi % x + n * xの範囲で自由に数を決めれる　mexの最大を目指せ
まずmodした時に0 ~ x - 1まで揃うか　揃わなければそこが穴
セグ木　は使う？
一番小さい穴はどこか
そこに数字があるかないかでBITを組む
揃ったら消す
"""

N, X = getNM()
cnt = [0] * (X + 1) # カウント数
layer = 0
bit = BIT(X) # 0かそれ以外か

for i in range(N):
    y = (getN() % X) + 1 # 1-index
    cnt[y] += 1
    # 数字を置いた場所に1を立てる
    if bit.cum(y, y + 1) == 0:
        bit.add(y, 1)
    # 揃ったので消す
    if bit.get(X + 1) == X:
        layer += 1 # あとで *= Xする
        # cntの全てから1を引く
        for i in range(1, X + 1):
            cnt[i] -= 1
            # もし1→0になったなら
            if cnt[i] == 0:
                bit.add(i, -1)

    # 一番小さい穴を探す
    ok, ng = 0, X + 1
    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        # これ以前の全ての場所にフラグが立っているか
        if bit.get(mid + 1) == mid:
            ok = mid
        else:
            ng = mid

    print(layer * X + ok)

# edufo E. String Reversal
# distinctでない場合の転倒数の求め方

"""
SをS#に変換するための最小スワップ回数
distinctでない場合の転倒数

['i', 'c', 'p', 'c', 's', 'g', 'u', 'r', 'u']
['u', 'r', 'u', 'g', 's', 'c', 'p', 'c', 'i']
一番近い値を持ってくる
swapは実際に行うとTLE
移動させるたびに元の位置にフラグを立てる

いつもは大きい値から順に
・自身の左にあるフラグ（自身より左にある自身より大きい数）を数える
・フラグを置く
をしていた
結局のとこiはi番目に置くことが確定しているのなら、小さい数字から順に
・最初の位置 + 追い抜かれた回数（自身より右にある自身より小さい数）- i
をしても良い

左にある自身より大きい数の総和 = 右にある自身より小さい数の総和
なのでdistinctでない場合左から順に
・一番左にあるS[i]の要素を取る
・最初の位置 + 追い抜かれた回数（自身より右にある自身より小さい数）- i
・フラグを立てる
をする
"""

N = getN()
S = [ord(s) - 97 for s in list(input())]
psuedo = S[::-1]

l = [deque([]) for i in range(26)]
for i in range(N):
    l[S[i]].append(i + 1) # BIT用に1-indexに

bit = BIT(N)
ans = 0
for i in range(N):
    # 一番近いものを取ってくる
    # その文字は現在　追い抜けれた回数 = 自分より右にあるこれまでに置いたもの
    # の数だけシフトしている
    # これをi番目に置く
    # ans += u + bit.cum(u, N + 1) - (i + 1)
    u = l[psuedo[i]].popleft()
    # print(u, bit.cum(u, N + 1), (i + 1), u + bit.cum(u, N + 1) - (i + 1))
    ans += u + bit.cum(u, N + 1) - (i + 1)
    bit.add(u, 1)

print(ans)
