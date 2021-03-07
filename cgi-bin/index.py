from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

N = 10
logk = N.bit_length()

# [Fi+2, Fi+1] = [[1, 1], [1, 0]][Fi+1, Fi]
# 一般項が出ない漸化式は行列の形に落とし込める
dp = [[[0, 0] for i in range(2)] for i in range(logk)]
dp[0] = [[1, 1], [1, 0]]

# 行列掛け算 O(n3)かかる
def array_cnt(ar1, ar2):
    h = len(ar1)
    w = len(ar2[0])
    row = ar1
    col = []
    for j in range(w):
        opt = []
        for i in range(len(ar2)):
            opt.append(ar2[i][j])
        col.append(opt)

    res = [[[0, 0] for i in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            cnt = 0
            for x, y in zip(row[i], col[j]):
                cnt += x * y
            res[i][j] = cnt
    return res

for i in range(1, logk):
    dp[i] = array_cnt(dp[i - 1], dp[i - 1])

# 行列の単位元
ans = [[1, 0], [0, 1]]
for i in range(logk):
    if N & (1 << i):
        ans = array_cnt(ans, dp[i])

# [Fi+2, Fi+1] = [[1, 1], [1, 0]][Fi+1, Fi]より
# [Fn+1, Fn] = A ** n[F1, F0] = A ** n[1, 0]
# Fn = ans[1][0] * 1 + ans[1][1] * 0
print(array_cnt(ans, [[1], [0]])[1][0])

# ABC113 D - Number of Amidakuji

H, W, K = getNM()
logk = H.bit_length()

if W == 1:
    print(1)
    exit()

mat = [[0] * W for i in range(W)]
# 列の数はH個
# うまく行列に
for bit in range(1 << (W - 1)):
    for i in range(1, (W - 1)):
        # 両方にフラグがあればとばす
        if bit & (1 << i) and bit & (1 << (i - 1)):
            break
    else:
        for i in range(W):
            if bit & (1 << i):
                # 目的地、出発地
                mat[i + 1][i] += 1
            # negative shiftしないよう
            elif i > 0 and bit & (1 << (i - 1)):
                mat[i - 1][i] += 1
            else:
                mat[i][i] += 1

dp = [[[0] * W for i in range(W)] for i in range(logk)]
dp[0] = mat

# 行列掛け算 O(n3)かかる
def array_cnt(ar1, ar2):
    h = len(ar1)
    w = len(ar2[0])
    row = ar1
    col = []
    for j in range(w):
        opt = []
        for i in range(len(ar2)):
            opt.append(ar2[i][j])
        col.append(opt)

    res = [[[0, 0] for i in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            cnt = 0
            for x, y in zip(row[i], col[j]):
                cnt += x * y
            res[i][j] = cnt
    return res

for i in range(1, logk):
    dp[i] = array_cnt(dp[i - 1], dp[i - 1])

# スタート地点
ans = [[0] * W]
ans[0][0] = 1
# 計算
for i in range(logk):
    if H & (1 << i):
        ans = array_cnt(ans, dp[i])

print(ans[0][K - 1] % mod)

# EDPC R - Walk

"""
通りの数を答える
同じ辺を複数回通ってもいい
長さKの有効パス　二分グラフとか？
Kがクソでか
ループで解けという
N <= 50 巡回セールスか
Kが小さいものを求める

dp iターン目にjにいる時、その通りは？
行列累乗する

4 2
0 1 0 0
0 0 1 1
0 0 0 1
1 0 0 0

0 1 2 3 縦に使う
0 - 1, 1 - 2, 1 - 3...

prev = [1, 1, 1, 1]
next[0] = 1 * 0 + 1 * 0 + 1 * 0 + 1 * 1
next[1] = 1 * 1 + 1 * 0 + 1 * 0 + 1 * 0
next[2] = 1 * 0 + 1 * 1 + 1 * 0 + 1 * 0
next[3] = 1 * 0 + 1 * 1 + 1 * 1 + 1 * 0
"""

N, K = getNM()
logk = K.bit_length()

mat = [getList() for i in range(N)]
dp = [[[0] * N for i in range(N)] for i in range(logk)]
dp[0] = mat

for i in range(1, logk):
    dp[i] = array_cnt(dp[i - 1], dp[i - 1])

ans = [[1] * N]
for i in range(logk):
    if K & (1 << i):
        ans = array_cnt(ans, dp[i])

print(sum(ans[0]) % mod)

"""
A, Cの長さは100 O(N ** 3)までいける
K + 1以降は自分で計算しろ　まともに1個ずつするのは無理　法則を見つけるかダブリングするか
3 5
10 20 30
7 19 13 の場合
A4 = 7 & 30 ^ 20 & 19 ^ 10 & 13
10 20 30 30
 7 19 13
A5は
10 [20 30 30]
 [7 19 13]
 7 & 30 ^ 19 & 30 ^ 13 & 20

for i in range(M - K):
    res = C[0] & A[-1]
    for j in range(1, K):
        res ^= (C[j] & A[-j - 1])
    A.append(res)

A[3] = (C[0] & A[2]) ^ (C[1] & A[1]) ^ (C[2] & A[0]) これを簡単にできないか
A[4] = (C[0] & A[3]) ^ (C[1] & A[2]) ^ (C[2] & A[1])

(C[0] & A[3]) = (C[0] & ((C[0] & A[2]) ^ (C[1] & A[1]) ^ (C[2] & A[0])))
論理積　全てにフラグが立っている場合に立つ

A[99] = (C[0] & A[98]) ^ (C[1] & A[97]) ^ (C[2] & A[96]) ^ (C[3] & A[95]) ^ (C[4] & A[94])
各数字が0か1なら
0 1 1
1 0 0 フラグが両方立っているときにしか反応しない　両方フラグが立っている本数は？
3 100
0 1 1
1 0 1
[0, 1, 1, 1,
 0, 1, 0,
 0, 1, 1, 1,
 0, 1, 0,
 0, 1, 1, 1,
 0, 1, 0...　周期性あり

[0, 1, 0, 1, 0,
 0, 1, 0, 1, 0,
 0, 1, 0, 1, 0,
 0, 1, 0, 1, 0,
 0, 1, 0, 1, 0, 0,

スライドした時のフラグの構成が同じであれば同じ結果がループされる
ローリングハッシュの要領

AND XORの半環の性質を使う
掛け合わせするCが固定なので行列累乗できるのん
ANDを掛け算、XORを足し算だと思え
[[0, 0, 7],
 [1, 0, 19],
 [0, 1, 13]] の行列を作る　最後の一項だけ計算す
計算は逆になる
"""

K, M = getNM()
A = getList()
C = getList()

if M <= K:
    print(A[M - 1])
    exit()

# 行列累乗
k = M - K
logk = k.bit_length()
dp = [[[0] * K for j in range(K)] for i in range(logk)]
# 初項を書き込む
for i in range(K - 1):
    dp[0][K - i - 2][i] = 2 ** 32 - 1
for i in range(K):
    dp[0][i][-1] = C[i]

def array_cnt(ar1, ar2):
    h = len(ar1)
    w = len(ar2[0])
    row = ar1
    col = []
    for j in range(w):
        opt = []
        for i in range(len(ar2)):
            opt.append(ar2[i][j])
        col.append(opt)

    res = [[[0, 0] for i in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            cnt = 0
            for x, y in zip(row[i], col[j][::-1]): # 計算は逆になる
                cnt ^= x & y # ここを変更
            res[i][j] = cnt
    return res

for i in range(1, logk):
    dp[i] = array_cnt(dp[i - 1], dp[i - 1])

ans = [A]
for i in range(logk):
    if k & (1 << i):
        ans = array_cnt(ans, dp[i])

print(ans[0][-1])

# ABC189 E - Rotate and Flip

"""
[x, y, 1]について変換する
1: xとyを交換してyを反転
[[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
2: xとyを交換してxを反転
[[0, -1, 0], [1, 0, 0], [0, 0, 1]]
3: xについて-x+2pに変換
[[-1, 0, 2p], [0, 1, 0], [0, 0, 1]]
4: yについて-y+2pに変換する
[[1, 0, 0], [0, -1, 2p], [0, 0, 1]]
"""

N = getN()
P = [getList() for i in range(N)]
M = getN()
manu = [getList() for i in range(M)]
Q = getN()
que = [getList() for i in range(Q)]

# M回の操作をまとめる
# 3 * 3のマトリックスを作る
dp = [[[0, 0, 0] * 3 for j in range(3)] for i in range(M + 1)]
dp[0] = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] # 単位行列
for i in range(M):
    if manu[i][0] == 1:
        dp[i + 1] = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
    elif manu[i][0] == 2:
        dp[i + 1] = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    elif manu[i][0] == 3:
        index, p = manu[i]
        dp[i + 1] = [[-1, 0, 2 * p], [0, 1, 0], [0, 0, 1]]
    else:
        index, p = manu[i]
        dp[i + 1] = [[1, 0, 0], [0, -1, 2 * p], [0, 0, 1]]
    dp[i + 1] = array_cnt(dp[i + 1], dp[i])

for m, p in que:
    x, y = P[p - 1]
    a_x, a_y, one_ = array_cnt(dp[m], [[x], [y], [1]]) # 縦は[[x], [y], [1]]みたいに
    print(a_x[0], a_y[0])
