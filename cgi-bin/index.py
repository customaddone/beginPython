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

N = 4
inf = float('inf')

d = [
[0, 2, inf, inf],
[inf, 0, 3, 9],
[1, inf, 0, 6],
[inf, inf, 4, 0]
]

dp = [[-1] * N for i in range(1 << N)]

def rec(s, v, dp):
    if dp[s][v] >= 0:
        return dp[s][v]
    if s == (1 << N) - 1 and v == 0:
        dp[s][v] = 0
        return 0
    res = float('inf')
    for u in range(N):
        if s & (1 << u) == 0:
            res = min(res,rec(s|(1 << u), u, dp) + d[v][u])
    dp[s][v] = res
    return res
# 結局のところ0からスタートしようが1からスタートしようが同じ道を通る
print(rec(0,0,dp))

# ABC054 C - One-stroke Path

N, M = getNM()
dist = [[] for i in range(N + 1)]
for i in range(M):
    a, b = getNM()
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

cnt = 0

pos = deque([[1 << 0, 0]])

while len(pos) > 0:
    s, v = pos.popleft()
    if s == (1 << N) - 1:
        cnt += 1
    for u in dist[v]:
        if s & (1 << u):
            continue
        pos.append([s | (1 << u), u])
print(cnt)

"""
全ての場所を一度だけ通り巡回する通りの数
bit(1 << N)を小さい順から探索する
①bit & (1 << 0)
最初に0を踏んでないということだから飛ばす
②現在の場所sを探すためN個探索する
③次の場所tを探すためN個探索する
④渡すdpする
"""

N, M = getNM()
G = [[0] * N for i in range(N)]
for i in range(M):
    a, b = getNM()
    G[a - 1][b - 1] = 1 # a ~ bのエッジが存在する
    G[b - 1][a - 1] = 1

# 状態bitから次の状態へ渡すdpするというのはよくやる
# [0](001) → [0, 1](011) → [0, 1, 2](111)
#          → [0, 2](101) → [0, 1, 2](111)
def counter(sta):
    # dp[bit][i]これまでに踏んだ場所がbitであり、現在の場所がiである
    dp = [[0] * N for i in range(1 << N)]
    dp[1 << sta][sta] = 1

    for bit in range(1, 1 << N):
        if not bit & (1 << sta):
            continue
        # s:現在の場所
        for s in range(N):
            # sを踏んだことになっていなければ飛ばす
            if not bit & (1 << s):
                continue
            # t:次の場所
            for t in range(N):
                # tを過去踏んでいない and s → tへのエッジがある
                if (bit & (1 << t)) == 0 and G[s][t]:
                    dp[bit|(1 << t)][t] += dp[bit][s]

    return sum(dp[(1 << N) - 1])

print(counter(0))

# ABC104 C - All Green
# 特別ボーナスがある問題は大抵bit dp
# 目標700点
D, G = getNM()
query = []
for i in range(D):
    p, c = getNM()
    query.append([i + 1, p, c])

ans_cnt = float('inf')

for bit in range(1 << D):
    sum = 0
    cnt = 0
    for i in range(D):
        if bit & (1 << i):
            sum += query[i][0] * query[i][1] * 100 + query[i][2]
            cnt += query[i][1]

    if sum < G:
        for j in range(D - 1, -1, -1):
            if not bit & (1 << j):
                left = G - sum
                fire = query[j][0] * 100
                opt = min(query[j][1], (left + fire - 1) // fire)
                sum += opt * query[j][0] * 100
                cnt += opt
                break

    if sum >= G:
        ans_cnt = min(ans_cnt, cnt)

print(ans_cnt)

# ABC119 C - Synthetic Kadomatsu
N, A, B, C = getNM()
L = getArray(N)

def counter(array):
    if (1 in array) and (2 in array) and (3 in array):
        opt = [0, 0, 0, 0]
        # 合成に10pかかる
        cnt = 0
        for i in range(len(array)):
            if opt[array[i]] > 0:
                cnt += 1
            if array[i] >= 1:
                opt[array[i]] += L[i]

        res = cnt * 10
        res += abs(opt[1] - A)
        res += abs(opt[2] - B)
        res += abs(opt[3] - C)

        return res

    else:
        return float('inf')

ans = float('inf')
def four_pow(i, array):
    global ans
    if i == N:
        ans = min(ans, counter(array))
        return
    # 4 ** Nループ
    for j in range(4):
        new_array = array + [j]
        four_pow(i + 1, new_array)

four_pow(0, [])
print(ans)

N, M = 4, 6
weight = [67786, 3497, 44908, 2156, 26230, 86918]
value = [[1, 3, 4], [2], [2, 3, 4], [2, 3, 4], [2], [3]]

# N個のものを全て手に入れるのに必要なコストの最小値
# コストを1にすれば最小個数がわかる
# Nの数が十分に小さいと使用可能
# Mの数が十分小さければMをbitdpする
def get_everything(n, weight, value):
    m = len(weight)
    dp = [float("inf")] * (1 << n)
    dp[0] = 0

    for i in range(m):
        bit = 0
        for item in value[i]:
            bit |= (1 << (item - 1))

        for j in range(1 << n):
            dp[j | bit] = min(dp[j | bit], dp[j] + weight[i])

    return dp[(1 << N) - 1]

ans = get_everything(N, weight, value)
if ans == float("inf"):
    print(-1)
else:
    print(ans)

# N:ブロックの個数 M;ブロックの色 Y:コンボボーナス Z:全色ボーナス
# N <= 5000, M <= 10
N, M, Y, Z = getNM()
# 色ボーナス
d = dict()
for i in range(M):
    c, p = input().split()
    d[c] = (i, int(p))
# 落ちてくるブロックの種類
B = input()

# 全通り出してみよう
# 2 ** N通り
# 単色でやってみる?
# どれを取ればいいか
# 前から順に＾
# どの色をコンボしても点数は同じ

# dp?

# dp[i][j]: 直前の色がi, 全部でjの色を使った
dp = [[-float('inf')] * (1 << M) for _ in range(M + 1)]
dp[M][0] = 0

# 交換するdpの要領
for e in B:
    # B[i]番目の色ポイント
    i, p = d[e]
    # 色iを含む状態について調べる
    # 色が少ないものから順に巻き込んでいく感じ
    for j in range((1 << M) - 1, -1, -1):
        if j & (1 << i) == 0:
            continue

        # 候補1: 直前の色が違うものだった and 以前に使った色を使った
        num1 = max(dp[k][j] for k in range(M + 1) if k != i) + p
        # 候補2: 直前の色が同じものだった
        num2 = dp[i][j] + p + Y
        # 候補3: 直前の色が違うものだった and 以前に使っってない色を使った
        num3 = max(dp[k][j ^ (1 << i)] for k in range(M + 1) if k != i) + p
        dp[i][j] = max(dp[i][j], num1, num2, num3)

# 全色ボーナス
for i in range(M):
    dp[i][(1 << M) - 1] += Z

ans = 0
for row in dp:
    ans = max(ans, max(row))
print(ans)

# JOI16 D-ぬいぐるみの整理 (Plush Toys)

# N個のぬいぐるみはM種類のうちのどれか
# 同じ種類のぬいぐるみが全て連続するように
N, M = getNM()
T = getArray(N)
T = [i - 1 for i in T]

# 20!は間に合わないが2 ** 20は間に合う
# 取り出すぬいぐるみの最小値
# ai, a2...と決めていった時
# 違う場所にあるものを全て取り出せばOK

# 20!を2 ** 20に改善する

cnt_toys = [0] * M # 種類iのぬいぐるみの数
cnt_acc = [[0] * (N + 1) for i in range(M)] # [l, r]の区間で種類iを指定した時に変えないといけないぬいぐるみの数


for i in range(M): # 種類
    for j in range(N): # 左から何番目のぬいぐるみ
        if T[j] != i:
            cnt_acc[i][j + 1] = 1
        cnt_acc[i][j + 1] += cnt_acc[i][j]
    cnt_toys[i] = N - cnt_acc[i][-1]

dp = [float('inf')] * (1 << M)
dp[0] = 0
# bit dpする
for s in range(1 << M):
    # 今まで置いてきたぬいぐるみの総計 左側に詰めて置く
    left = sum([cnt_toys[i] for i in range(M) if s & (1 << i)])
    # 種類jを新たにその右に置く
    for j in range(M):
        if s & (1 << j):
            continue
        length = cnt_toys[j]
        cnt = cnt_acc[j][left + length] - cnt_acc[j][left] # 今まで置いてきたぬいぐるみの右側に種類jのぬいぐるみを指定する
        dp[s | (1 << j)] = min(dp[s | (1 << j)], dp[s] + cnt)

print(dp[-1])

# 天下一プログラマーコンテスト2014予選A C - 天下一文字列集合

"""
英小文字は26文字
ワイルドカード部分は無視していい
Pの全ての要素が入っているようなX = ['????', '????'...]の要素の最小値を求めよ
二分探索したくなる

まずは愚直に
a*x*
*xx*
*x*b
**cb
**** の場合

1: a*x*
X = [a*x*]を用意する
2: *xx*
a*x*が使えそうなのでX = [axx*]
3: *x*b
axx*が使えそうなのでX = [axxb]
4: **cb
axxbは使えない　X = [axxb, **cb]を置く
そもそもNが小さい
X = [a*x*, *xx*, *x*b, **cb, ****]を用意して適当にjointする
結合しなかったらout
計算量はN ** N * M 間に合わない
無駄な部分を減らす　計算量を落とそう
矛盾するものを組み合わせても当然ダメ
グループ1: [a*x*]
グループ2: [**cb]
disjointするグループは別に置く

どれとどれが矛盾しないか
グループ内の任意の２つが矛盾しなければひとまとまりにできる
全探索かunionか
ベースとなる7つを選ぶ　とすると
14C5が2002
14C6が3003
14C7が3432
14C8が3003
14C9が2002
jointするもの同士だけでグループを作る
bit全探索でグループを２つにできる
"""

N, M = getNM()
word = [list(input()) for i in range(N)]

# 判定
same = [[0] * N for _ in range(N)]
for i in range(N - 1):
    S = word[i]
    for j in range(i + 1, N):
        T = word[j]
        isOK = 1
        for s, t in zip(S, T):
            if s == t:
                continue
            if s == "*" or t == "*":
                continue
            isOK = 0
            break
        same[i][j] = isOK

# どの文字iの組み合わせで１つの集合を作れるか
dp = [N] * (1 << N)
for bit in range(1 << N):
    bl = 1
    for i in range(N - 1):
        if (bit >> i) & 1:
            for j in range(i + 1, N):
                if (bit >> j) & 1:
                    bl &= same[i][j]
    if bl:
        dp[bit] = 1

# あとはget_everythingみたいに
for bit in range(1 << N):
    sub = bit
    while True:
        dp[bit] = min(dp[bit], dp[sub] + dp[bit & ~sub])
        sub = (sub - 1) & bit
        if bit == sub:
            break

print(dp[(1 << N) - 1])

# edufo70 D. Minimax Problem

"""
２つの配列を見比べる
5 0 3 1 2
1 8 9 1 3 ２つの要素の大きい方をとる
5 8 9 1 3 その最小値がこの組み合わせの答え　その最大値は？
愚直O(N^2M)

最小値がiである条件は？　両方がi以下であるポイントが最低1つあること
小さい順に置いていく
置いていった時に置いている場所がダブらない2つが答え bitmask
置く回数が多くなりそう　N2^Mなら届く　候補になり得ないものはあらかじめ落とす

というか候補は最高256個なのでそんなに判定はいらない
二分探索が必要
置くNM + 判定2^M
NMlogN

x以下の要素を全て置いた時、互いにダブらないペアがある
valはx以上であることが保証される
"""

N, M = getNM()
A = [getList() for i in range(N)]
if N == 1:
    print(1, 1)
    exit()

def f(x):
    bit = [0] * N
    bit_cnt = [0] * (1 << M)
    bit_cnt[0] = N # 最初は全て0

    for i in range(N):
        for j in range(M):
            if A[i][j] <= x:
                bit_cnt[bit[i]] -= 1
                bit[i] += (1 << j)
                bit_cnt[bit[i]] += 1

    repre = [[] for i in range(1 << M)]
    for i in range(N):
        repre[bit[i]].append(i)

    res, p1, p2 = 0, -1, -1
    if bit_cnt[0] >= 2:
        return 1, repre[0][0], repre[0][1]

    # bit全探索 ダブらない奴があるか
    for b in range(1 << M):
        ene = (1 << M) - 1 - b
        e = ene
        # eneの部分集合について探索
        while e:
            if bit_cnt[b] and bit_cnt[e]:
                res = 1
                p1, p2 = repre[b][0], repre[e][0]
            e -= 1
            e &= ene

    return res, p1, p2

# 二分探索
ok, ng = 0, 10 ** 9 + 7
while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    jud, p1, p2 = f(mid)
    if jud == 1:
        ok = mid
    else:
        ng = mid

jud, p1, p2 = f(ok)
if jud:
    print(p1 + 1, p2 + 1)
else:
    print(1, 2)
