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

### Typical DP Contest

# A - コンテスト
# 部分和問題

N = getN()
P = getList()

prev = [0] * 10001
prev[0] = 1

for i in range(N):
    next = [0] * 10001
    for j in range(10001):
        next[j] = prev[j]
        if j - P[i] >= 0:
            next[j] = max(next[j], prev[j - P[i]])
    prev = next
print(sum(prev))

# B - ゲーム

A, B = getNM()
L_a = getList()
L_b = getList()

# dp[i][j] = i,jとった状態を初期状態としてスタートした場合のぬの得られる最大得点
dp = [[0] * (B + 1) for _ in range(A + 1)]
dp[A][B] = 0

# https://www.creativ.xyz/tdpc-b-684/
# 逆から
# すめけ君の点数はsum(L_a + L_b) - すぬけ君の合計
# すめけ君はすぬけ君の点数を最小化するよう動く
for i in range(A, -1, -1):
    for j in range(B, -1, -1):
        if (i == A and j == B):
            continue
        if not (i + j) % 2:
            if i == A:
                dp[i][j] = dp[i][j + 1] + L_b[j]
            elif j == B:
                dp[i][j] = dp[i + 1][j] + L_a[i]
            else:
                # 遷移元はdp[i + 1][j], dp[i][j + 1]
                dp[i][j] = max(dp[i + 1][j] + L_a[i], dp[i][j + 1] + L_b[j])
        else:
            if i == A:
                dp[i][j] = dp[i][j + 1]
            elif j == B:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = min(dp[i][j + 1], dp[i + 1][j])

print(dp[0][0])

# C - トーナメント
# 確率dp
# 試合iで選手1が勝つ確率、選手2が勝つ確率...選手1 << Kが勝つ確率

K = getN()
bit = 1 << K
R = getArray(bit)

dp = [[0] * bit for i in range(bit * 2)]

for i in range(bit):
    dp[i + bit][i] = 1

#         1
#       2   3
#      4 5 6 7
# みたいなトーナメントを考える
# ビットシフトの関係でbitは１から始めた方が都合がいい
for i in range(bit - 1, 0, -1):
    for j in range(bit):
        # もし左側の方のトーナメントを勝ち進んでいたら
        if dp[i << 1][j] > 0:
            # j vs l
            prob = 0
            for l in range(bit):
                if j == l or dp[(i << 1) + 1][l] == 0:
                    continue
                prob += (1 / (1 + 10 ** ((R[l] - R[j]) / 400))) * dp[(i << 1) + 1][l]
            dp[i][j] = prob * dp[i << 1][j]
        # もし右側の方のトーナメントを勝ち進んでいたら
        elif dp[(i << 1) + 1][j] > 0:
            # j vs l
            prob = 0
            for l in range(bit):
                if j == l or dp[i << 1][l] == 0:
                    continue
                prob += (1 / (1 + 10 ** ((R[l] - R[j]) / 400))) * dp[i << 1][l]
            dp[i][j] = prob * dp[(i << 1) + 1][j]

for i in dp[1]:
    print(i)

# D - サイコロ
# 大きい数字は因数で持つ

N, D = getNM()

def spliter(n, split):
    splited = n
    cnt = 0

    while splited % split == 0:
        if splited == 0:
            break
        splited //= split
        cnt += 1
    # print(cnt)
    return splited, cnt

D, two = spliter(D, 2)
D, three = spliter(D, 3)
D, five = spliter(D, 5)

# 2, 3, 5以外の因数が混じっている場合は作れない
if D != 1:
    print(0)
    exit()

# dp[i][two][three][five]: サイコロをi回振った時、
# 出た目の積が2 ** two * 3 ** three * 5 * fiveである
prev = [[[0] * (five + 1) for i in range(three + 1)] for j in range(two + 1)]
prev[0][0][0] = 1

for i in range(N):
    next = [[[0] * (five + 1) for i in range(three + 1)] for j in range(two + 1)]
    for tw in range(two + 1):
        for th in range(three + 1):
            for fi in range(five + 1):
                # 1
                next[tw][th][fi] += prev[tw][th][fi]
                # 2
                next[min(two, tw + 1)][th][fi] += prev[tw][th][fi]
                # 3
                next[tw][min(three, th + 1)][fi] += prev[tw][th][fi]
                # 4
                next[min(two, tw + 2)][th][fi] += prev[tw][th][fi]
                # 5
                next[tw][th][min(five, fi + 1)] += prev[tw][th][fi]
                # 6
                next[min(two, tw + 1)][min(three, th + 1)][fi] += prev[tw][th][fi]

    prev = next

print(prev[two][three][five] / pow(6, N))

# E-数　
# 桁dp

D = getN()
N = input()

def digit_dp_2(n, k):
    l = len(n)

    dp = [[[0] * (k + 1) for _ in range(2)] for i in range(l + 1)]
    dp[0][0][0] = 1

    for i in range(l):
        d = int(n[i])

        for j in range(2):
            for d_j in range(10 if j else d + 1):
                # mod k_j
                for k_j in range(k + 1):
                    dp[i + 1][j | (d_j < d)][(k_j + d_j) % D] += dp[i][j][k_j]
                    dp[i + 1][j | (d_j < d)][(k_j + d_j) % D] %= mod

    return dp

dp = digit_dp_2(N, D)
print((dp[-1][0][0] + dp[-1][1][0]) % mod - 1) # 0は除く

# F - 準急

N, K = getNM()
# 連続するK個
# dp[i]:iまでの間での通り
# 遷移の方法は
# dp[i - 1] * 止まる/止まらない
# 止まる場合に制限がある
# dp[i] = dp[i - 1] * ?(止まる) + dp[i - 1](止まらない)

dp1 = [0] * (N + 1)  # dp1[i] = (駅iまでで条件を満たす停車駅の組合せ、但し駅iは停車せず)
dp2 = [0] * (N + 1)  # dp2[i] = (駅iまでで条件を満たす停車駅の組合せ、但し駅iは停車)
dp1[0] = 1
dp2[1] = 1
for i in range(2, N + 1):
    dp1[i] = dp1[i - 1] + dp2[i - 1]
    if i - K >= 0:
        # dp2[i]を考える時、dp1[i - K]:一番最後に止まらなかったがi - Kでの時を考える
        # この時i - Kからi - 1までK回連続で止まる通りは
        # dp1[i - K] * 1(i - K + 1で止まる) * 1(i - K + 2で止まる)...のdp1[i - K]通り
        # これをdp2[i - 1]から引く
        # dp2[i - K]に含まれるものは以前のどこかdp2[i - 1], dp2[i - 2]で引いている
        dp2[i] = dp1[i - 1] + dp2[i - 1] - dp1[i - K]
    else:
        dp2[i] = dp1[i - 1] + dp2[i - 1]
    dp1[i] %= mod
    dp2[i] %= mod

print(dp2[-1])

# G - 辞書順

S = input()
K = getN()
N = len(S)
# i文字目以降で最初に
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alp = {}
for i in range(26):
    alp[alphabet[i]] = i
S = [alp[S[i]] for i in range(N)] # pypyだと遅いので

def changer(i, j):
    return i * 26 + j
# i文字目以降について文字cから始まる部分文字列の個数
dp = [0] * (N + 1) * 26 # 1次元配列にしないとメモリ容量の関係で無理
dp[changer(N - 1, S[N - 1])]= 1

for i in range(N - 2, -1, -1):

    for j in range(26):
        # S[i]と一致しない場合
        if S[i] != j:
            dp[changer(i, j)] += dp[changer(i + 1, j)] # 前のを引き継ぐだけ
        # 一致する場合
        else:
            dp[changer(i, j)] += 1 # 後に何も足さないケース
            dp[changer(i, j)] += sum(dp[changer(i + 1, 0):changer(i + 2, 0)]) # S[i] + 今まで出た全てのケースを足すå

part_sum = sum(dp[:26])
if part_sum < K:
    print('Eel')
    exit()

res = ""
i = 0

while i < N:
    for j in range(26):
        if K - dp[changer(i, j)] <= 0:
            break
        K -= dp[changer(i, j)] # K >= dp[i][j]ならそのケースはK番目より前にあるので飛ばす
    res += alphabet[j] # jが次の文字
    K -= 1 # jを選んで dp[i][j]については終了
    if K <= 0: # K <= 0ならもう足さなくていい
        break
    while S[i] != j: # S[i]が足した文字jと一致するまでS[i]を進める
        i += 1
    i += 1 # 次はS[i + 1]から探索する
print(res)

# H - ナップザック
# 種類数が絡む

N, W, C = getNM()
M = 50
item = [[] for _ in range(M)]
for _ in range(N):
    w, v, c = getNM()
    item[c - 1].append((w, v))


dp = [[-float('inf')] * (W + 1) for _ in range(C + 1)]
dp[0][0] = 0
# 各色の商品について調べる
for i in range(M):
    # dpを更新していく
    for c in range(C, 0, -1):
        tmp = [-float('inf')] * (W + 1)
        # 色iの各商品について
        for x, y in item[i]:
            for w in range(W, -1, -1):
                if w - x >= 0:
                    # dpの情報がtmpにレコードされる
                    tmp[w] = max(tmp[w], dp[c - 1][w - x] + y, tmp[w - x] + y)

        # 比較する
        for w in range(W + 1):
            dp[c][w] = max(tmp[w], dp[c][w])

print(max(max(dp[c]) for c in range(C + 1)))

# i-イウイ
# 区間dp

S = input()
N = len(S)

dp = [[-1] * (N + 1) for _ in range(N + 1)]

def dfs(l, r, dp):
    if dp[l][r] >= 0:
        return dp[l][r]

    if r - l < 3:
        dp[l][r] = 0
        return dp[l][r]

    if r - l == 3:
        if S[l:r] == 'iwi':
            dp[l][r] = 3
        else:
            dp[l][r] = 0
        return dp[l][r]

    ans = 0
    # 区間のどこかに区切りを作る
    for mid in range(l + 1,r): # 区切りはl + 1...r - 1のどこか
        ans = max(ans, dfs(l, mid, dp) + dfs(mid, r, dp))
        # 最適な区切り方が見つかれば即break
        if S[l] == 'i' and  S[mid] == 'w' and S[r - 1] == 'i':
            if dfs(l + 1,mid,dp) == mid - l - 1 and dfs(mid + 1,r - 1,dp) == r - mid - 2:
                ans = r - l
                break
    dp[l][r] = ans
    return ans

ans = dfs(0, N, dp)//3
print(ans)

# K-ターゲット

N = getN()
# 座標xにあり、半径r
# ri - (xi - xi-1) - ri-1 > 0ならCi-1はCiの内部に含まれる
# ri + xi-1 > ri-1 + xiなら
circle = []
for i in range(N):
    x, r = getNM()
    circle.append([x - r, x + r]) # 端点のみ抑える

# N <= 10 ** 5なので最大流無理
# 貪欲?

# もしleftが同じならrightが小さい順に（小→大へ更新していく）
circle.sort(key = lambda i: i[1])
# lが小さい順に並ぶ
circle.sort(key = lambda i: i[0])

# うまく並び変えたあと右端の点のみ取りLIS
r_list = []
for i in range(N):
    r_list.append(-circle[i][1])

def lis(A):
    L = [A[0]]
    for a in A[1:]:
        # Lの末尾よりaが大きければ増加部分を拡張できる
        if a > L[-1]:
            # 前から順にLに追加していく
            L.append(a)
        else:
            L[bisect_left(L, a)] = a

    # Lの配列の長さは求まる
    # Lの中身はデタラメ
    return len(L)
print(lis(r_list))

# L - 猫

N = getN()
F = []
for _ in range(N):
    F.append(getList())

cs = []
for i in range(N):
    line = [0] * (N + 1)
    for j in range(N):
        line[j + 1] = line[j] + F[i][j]
    cs.append(line)
dp = [[-float('inf')] * N for _ in range(N)]
dp[1][0] = F[1][0]
dp[1][1] = 0
for i in range(2, N):
    ma = -float('inf')
    for j in range(i + 1):
        ma = max(ma, dp[i - 1][j])
        dp[i][j] = max(dp[i][j], ma + cs[i][i] - cs[i][j])
print(max(dp[-1]) * 2)

# M-家
# 巡回セールスマン + 行列累乗　

H, R = getNM()
G = [getList() for i in range(R)]

matrix = [[0] * R for _ in range(R)]
# staから1, 2...Rまで巡回する通り
def counter(sta):
    dp = [[0] * R for i in range(1 << R)]
    dp[1 << sta][i] = 1
    for bit in range(1, 1 << R):
        if not bit & (1 << sta):
            continue
        for s in range(R):
            if bit & (1 << s):
                for t in range(R):
                    if (bit & (1 << t)) == 0 and G[s][t]:
                        dp[bit|(1 << t)][t] = (dp[bit|(1 << t)][t] + dp[bit][s]) % mod

    for bit in range(2 ** R):
        for j in range(R):
            matrix[i][j] = (matrix[i][j] + dp[bit][j]) % mod

# 行列生成
for i in range(R):
    counter(i)

# matrixをH回[1, 0, 0...]にかける
logk = H.bit_length()
dp = [[[0] * R for i in range(R)] for i in range(logk)]
dp[0] = matrix

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
            # 今回modをつける
            res[i][j] %= mod
    return res

for i in range(1, logk):
    dp[i] = array_cnt(dp[i - 1], dp[i - 1])

# 行列の単位元
ans = [[0] * R]
ans[0][0] = 1

for i in range(logk):
    if H & (1 << i):
        ans = array_cnt(ans, dp[i])

print(ans[0][0] % mod)

# O - 文字列
# 組み合わせdp

"""
# 一個飛ばしでボールを置く通りの数
def counter(n, s):
    # dp[i][j][k]: i個目まで進めた時にj個まで置いている通りの数
    dp = [[[0, 0] for _ in range(s + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    for i in range(1, n + 1):
        for j in range(s + 1):
            # ボールを置かない
            dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1])
            # ボールを置く
            # 前でボールを置いていない場合のみ置ける
            dp[i][j][1] = dp[i - 1][j - 1][0]
    return sum(dp[n][j])
"""

freq = getList()
freq = [f for f in freq if f > 0]

N = len(freq)
S = sum(freq)

"""
既存の文字列のどこに新しい文字を挿入するか、という思考をする。
同じ文字が隣り合っている箇所に挿入するのか否か？　
#dp[i][j] -> i種類目の文字まで見る。同じ文字が隣り合っている箇所がj箇所存在する。
何分割するか？　同じ文字が隣り合っている箇所のうち、何か所に挿入するか？
分割数の上限は、既存の文字列の長さ+1 か　文字の長さ
同じ文字が隣り合っている箇所のうち、何か所に挿入するかの上限は、同じ文字が隣り合っている箇所か分割数
何分割するか、どこで分割するか、同じ文字がとなり合う箇所に何か所に挿入するか、どこに挿入するか
"""

dp = [[0] * S for _ in range(N)]

f = freq[0] # １番目の文字が何個あるか
dp[0][f - 1] = 1 # 1番目の文字を入れた後、同じ文字が隣り合ってる場所が(１番目の文字の個数 - 1)個ある

memo = [[0] * 12 for _ in range(261)]

# 逆元事前処理ver
# nが小さい場合に
lim = 10 ** 5 + 1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    # 累計
    factinv.append((factinv[-1] * inv[-1]) % mod)

def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod

s = 0
for i in range(N - 1):
    # i + 1についてレコードしていく
    s += freq[i] # i番目までの文字の個数の総数
    f = freq[i + 1] # i + 1番目の文字の個数

    # j: 隣合う箇所(0個 ~ 260個ある)
    for j in range(S):
        # d:分割数の個数
        # ただし分割数の上限はこれまで出てきた文字の個数 + 1個まで
        # これまで出てきた文字: ?
        # ○?○?○○
        for d in range(1, min(f, s + 1) + 1):
            # k:隣り合う箇所をいくつ潰すか
            # ただし潰す個数の上限は分割dの個数
            for k in range(min(j, d) + 1):
                # d - kがs - jを上回るケースがあるので排除する
                if d - k <= s + 1 - j:
                    # 分割したd個のうちk個を使ってj個の隣り合う箇所のうちk個潰す
                    # dp[i + 1][j + (f - d) - k]:j個の隣り合う箇所のうちk個潰す、ただし新しく追加した文字が内包する
                    # 隣り合う個数の数(f - d)を足す

                    # cmb(j, k):j個の隣り合う箇所のうちk個潰す地点を決める
                    # cmb(f - 1, d - 1): f - 1個の分割ポイントのうちd - 1個に仕切りを置く　これによりd個に分割できる
                    # cmb(s + 1 - j, d - k):隣合わない部分 + 1に余ったd - kを入れる
                    dp[i + 1][j + (f - d) - k] += dp[i][j] * cmb(j, k) * cmb(f - 1, d - 1) * cmb(s + 1 - j, d - k)

print(dp[-1][0] % mod)
