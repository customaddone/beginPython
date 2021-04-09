from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product
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
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
MOD = 998244353
INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

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

# EDPC O - Matching

"""
N組のペアを作る通りは何通りか
dpかcomboか
3
0 1 1
1 0 1
1 1 1 1, 2, 3は誰とでもペアになれる

bitでやる
1111....全ての人がペアになっている通り
2 ** 21 = 2000000ぐらい　遷移の方法がわからない
0 1 1 の 1からどれか1つ選ぶ
1 0 1 の 1からどれか1つ選ぶ

トポロジカルに
"""

N = getN()
maze = [[int(j) for j in list(input().split())] for i in range(N)]

# ビットフラグの少ない順にソート
bi = [[] for i in range(N)]
for bit in range((1 << N) - 1):
    bi[bin(bit).count('1')].append(bit)

prev = [0] * (1 << N)
prev[0] = 1

for i in range(N):
    next = [0] * (1 << N)
    for bit in bi[i]:
        for j in range(N):
            if maze[i][j]:
                next[bit | (1 << j)] += prev[bit]
                next[bit | (1 << j)] %= mod

    prev = next

print(prev[-1])

# EDPC U - Grouping

"""
N羽のウサギをいくつかのグループに分ける
いくつか bit dpできない
グループの分け方を考える dpの遷移方法は
N!で出来るなら話は早い　2 ** Nに落とすのか
範囲を絞って全探索したいが
うさぎ1 を入れる
うさぎ2 を1と同じにするか　別のに入れるか
うさぎ3 を1と同じにするか, 2と同じにするか,
bit dp で１グループあたりのパーツは揃う
どのようにパーツを合わせるか
2 ** 16 = 65536

0000010000について
0の部分が可変 0か1か
0000010111 は 0000010000と0000000111を組み合わせられる
dpを更新していく
一番きつそうなフラグ8本でも16C8 * 2 ** 8 = 330万ぐらい
C - 天下一文字列集合みたいな感じ
"""

N = getN()
A = [getList() for i in range(N)]

dp = [0] * (1 << N)

# まず元となるパーツを全て作る
for bit in range(1, 1 << N):
    res = 0
    for i in range(N):
        for j in range(i + 1, N):
            if bit & (1 << i) and bit & (1 << j):
                res += A[i][j]
    dp[bit] = res

# dpを更新していく
for bit in range(1, 1 << N):
    ene = [0] # 相手を作る
    for i in range(N):
        if not bit & (1 << i):
            for j in range(len(ene)):
                ene.append(ene[j] + (1 << i))
    # dp更新
    for e in ene:
        dp[bit + e] = max(dp[bit + e], dp[bit] + dp[e])

print(dp[-1])

# ARC100 E - Or Plus Max

"""
A = {0, 1, 2}
冪集合 = {}, {0}, {1}, {2}, {0, 1}...
f = [3, 1, 4, 1, 5...]

ある部分集合Siについて, Si <= Tとなる全てのf(T)の総和を求めたい
Si = {1} Siが含まれるもの全ての和
T = {1}, {0, 1}, {1, 2}, {0, 1, 2}
逆verもある Siの部分集合全てについて
Siの補集合を取ってゼータ変換をする

Siを部分集合にするものについて
n = 3  # 集合の要素数
dp = [3, 1, 4, 5, 1, 9, 2, 6]  # 2^n の長さ

for j in range(n):
    bit = 1 << j
    for i in range(1 << n): # 小さい順からやる
        if i & bit == 0: # 重ならないなら
            # i | bitよりサイズが一つ小さい部分集合に自身を足す
            # N回やることで条件を満たす全ての要素について操作できた
            dp[i] += dp[i | bit]

print(dp)
# => [31, 21, 17, 11, 18, 15, 8, 6]

Siの各部分集合について
n = 3  # 集合の要素数
dp = [3, 1, 4, 5, 1, 9, 2, 6]  # 2^n の長さ

for j in range(n):
    bit = 1 << j
    for i in range(1 << n):
        if i & bit:
            dp[i] += dp[i ^ bit]

print(dp)
# => [3, 4, 7, 13, 4, 14, 10, 31]
0b1 0b0
0b11 0b10
0b101 0b100
0b111 0b110
0b10 0b0
0b11 0b1 要素0b0の情報も持つ
0b110 0b100
0b111 0b101 要素0b100の情報も持つ
0b100 0b0
0b101 0b1
0b110 0b10 要素0b0の情報も持つ
0b111 0b11 要素0b0, 0b1の情報も持つ

0b111に各要素1回きり情報が伝播する

総和の値から元の値を割り出すのがメビウス変換
"""

N = getN()
dp = getList()
que = [[dp[i], 0] for i in range(1 << N)]

def merge(q1, q2):
    res = q1 + q2
    return sorted(res)[-2:]

# 高速ゼータ変換
for j in range(N):
    bit = 1 << j
    for i in range(1 << N):
        if i & bit:
            que[i] = merge(que[i], que[i ^ bit])

ans = []
for q in que[1:]:
    if ans:
        ans.append(max(ans[-1], q[0] + q[1]))
    else:
        ans.append(q[0] + q[1])

for a in ans:
    print(a)
