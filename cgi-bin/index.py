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
sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# ARC060 E 高橋君とホテル

"""
クエリがたくさん
それぞれlogNで処理しろ
愚直な方法は
方向は逆にしても同じ結果
要するにオーバーしてもいい

最大N - 1回飛べる
"""

N = getN()
A = getList()
D = getN()
Q = getN()
que = [getList() for i in range(Q)]

dest = [0] * N
r = 0
# 一回でどこまで飛べるか
for l in range(N):
    while r < N and A[r] - A[l] <= D:
        r += 1
    dest[l] = r - 1

logn = N.bit_length()
# 2 ** N回飛んでどこまで行けるか
doubling = [[0] * N for i in range(logn)]
doubling[0] = dest

for i in range(1, logn):
    for j in range(N):
        # 前回の時点ですでに欄外に飛んでる場合
        if doubling[i - 1][j] == N:
            doubling[i][j] = N
        # それ以外はダブリング
        else:
            doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

# ギリギリ超えないところを探す
for a, b in que:
    if a > b:
        a, b = b, a
    a -= 1
    b -= 1
    # 計算
    cnt = 0
    now = a
    for j in range(logn - 1, -1, -1):
        # ゴールまで辿りつく前まで進む
        if doubling[j][now] < b:
            cnt += 1 << j
            now = doubling[j][now]

    # 限界まで近づいた後 +1する
    print(cnt + 1)

# cf744 F. Array Stabilization (AND version)

"""
replaced by
回転してANDをとる　これを繰り返して全部0になるか
andする そこにaiとadiのどちらかが0なら0になる
aiはそのうち消えるか
回転させるとは d個先のフラグを見るということ
フラグが立っていなければ消える
greedyにやりたいが
d = 2
一巡後にフラグが立っている
a[0] = 1かつa[2] = 1
二順後にa[0]にフラグが立っている:
a[0] = 1かつa[2] = 1かつa[4] = 1 (a[2]は1順目にa[4]を参照しているため)

つまりa[0]がn順後にフラグが立っている条件は
a[0] ~ a[d * n]番目までが全て1である必要がある

-1になる条件　ループする
nがdで割り切れる　その剰余項グループ内のフラグが全て1であるグループがあるとNG

そうでないなら一個ずつフラグを消していく
一番最後に生き残るフラグを探せばいいのでは 1で繋いでいく作業

ダブリングしていけばlogN
t回dを飛ぶとき何個1が続いているか
現在のポイントは何順後に0になっているか　二分探索
"""

T = getN()
for _ in range(T):
    N, D = getNM()
    A = getList()
    logk = 32
    doubling = [[-1] * N for _ in range(logk)]
    for i in range(N):
        # D個先にフラグがある
        if A[i] == 1 and A[(i + D) % N] == 1:
            doubling[0][i] = (i + D) % N
        else:
            doubling[0][i] = -1

    for i in range(1, logk):
        for j in range(N):
            # 飛べない
            if doubling[i - 1][j] == -1:
                doubling[i][j] = -1
            # それ以外はダブリング
            else:
                doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

    ans = -1
    for i in range(N):
        if A[i] == 0:
            continue
        now = i
        cnt = 0
        for j in range(logk - 1, -1, -1):
            if doubling[j][now] != -1:
                cnt += 1 << j
                now = doubling[j][now]
        ans = max(ans, cnt)

    if ans == 2 ** 32 - 1:
        print(-1)
    else:
        print(ans + 1)
