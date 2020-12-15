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

# ABC004 マーブル
R, G, B = getNM()

dp = [[float('inf')] * (R + G + B + 1) for i in range(2001)]
dp[0][R + G + B] = 0

# 残り個数により置くボールの色が変化する
# ボールを置くコストも変化する
def judge(point, ball):
    if ball > G + B:
        return abs(point - (-100))
    elif G + B >= ball > B:
        return abs(point)
    else:
        return abs(100 - point)

for i in range(1, 2001):
    for j in range(R + G + B, -1, -1):
        if j == R + G + B:
            dp[i][j] = dp[i - 1][j]
        else:
            # i - 1000の地点にj + 1ボールを置き,残りはj個
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1] + judge(i - 1000, j + 1))
print(dp[2000][0])

# ABC017 D - サプリメント

"""
通りの数を求める
dpかcombo
1日目 1 or 1, 2食べる 尺取りっぽい
1日目 1の時　2日目 2 or 2, 1
1日目 1, 2の時、2日目 1 or 1, 2
1: 1, 2 2: 1と1: 1, 2: 2, 1は通りが異なるが、次からの遷移は同じ
dpっぽい
dp[i]: 前日までにiまで食べる通り
dp[0] = 1
dp[1] = 1 前回のゴールは0番目
dp[2] = 2 前回のゴールは0番目、1番目
dp[3] = 3 前回のゴールは1,2番目
dp[4] = 5 前回のゴールは2,3番目
dp[5] = 5 前回のゴールは4番目
累積すればbitいらない
"""

N, M = getNM()
F = getArray(N)
dp = [0] * (N + 2) # imosとして使う 2-index
dp[0] = 0
dp[1] = 1

dict = defaultdict(int)
l = 0
for r in range(N):
    # 尺取り
    while dict[F[r]] == 1:
        dict[F[l]] -= 1
        l += 1
    dict[F[r]] += 1

    dp[r + 1] += dp[r] # 累積
    # 範囲内を足す
    dp[r + 2] += (dp[r + 1] - dp[l])
    dp[r + 2] %= mod

print(dp[-1] % mod)

# ABC044 C - 高橋君とカード
# 平均はQ[i] -= Aしとく
N, A = getNM()
Q = getList()
for i in range(N):
    Q[i] -= A

dp = [[0] * 5002 for i in range(N + 1)]
dp[0][2501] = 1

for i in range(1, N + 1):
    for j in range(5002):
        dp[i][j] += dp[i - 1][j]
        if 0 <= j - Q[i - 1] <= 5001:
            dp[i][j] += dp[i - 1][j - Q[i - 1]]

print(dp[-1][2501] - 1)

# ABC071 D - Coloring Dominoes
N = getN()
S1 = input()
S2 = input()
dp = [0 for i in range(N)]
if S1[0] == S2[0]:
    dp[0] = 3
else:
    dp[0] = 6
# i - 1個目、i個目が
# 横ドミノ１個目→横ドミノ２個目
# 横ドミノ→横ドミノ
# 横ドミノ→縦ドミノ
# 縦ドミノ→縦ドミノ
# 縦ドミノ→横ドミノそれぞれについて場合分け
# 各回について
for i in range(1, N):
    # 横ドミノ２つ目だった場合
    if S1[i] == S1[i - 1]:
        dp[i] = dp[i - 1]
    # 横ドミノ１つめor縦ドミノ１つ目の場合
    else:
        # 縦ドミノ１つ目
        if S1[i] == S2[i]:
            # 一つ前も縦ドミノ
            if S1[i - 1] == S2[i - 1]:
                dp[i] = (dp[i - 1] * 2) % mod
            # 横ドミノ
            else:
                dp[i] = dp[i - 1]
        # 横ドミノ1つ目
        else:
            # 一つ前が縦ドミノ
            if S1[i - 1] == S2[i - 1]:
                dp[i] = (dp[i - 1] * 2) % mod
            # 一つ前が２つ目横ドミノ
            else:
                dp[i] = (dp[i - 1] * 3) % mod
print(dp[-1])

# ABC074 C - Sugar Water
# ABが水、CDが砂糖、Eがとけられる量、Fが上限
A, B, C, D, E, F = getNM()

# A,Bを好きな回数使うことでi(0 <= i <= 30)の水を作り出せる
dp1 = [0] * 31
dp1[0] = 1
for i in range(1, 31):
    if i >= A:
        dp1[i] = max(dp1[i], dp1[i - A])
    if i >= B:
        dp1[i] = max(dp1[i], dp1[i - B])
waterlist = []
for i in range(31):
    if dp1[i] > 0:
        waterlist.append(i)

# C,Dを好きな回数使うことでi(0 <= i <= 3000)の砂糖を作り出せる
dp2 = [0] * 3001
dp2[0] = 1
for i in range(1, 3001):
    if i >= C:
        dp2[i] = max(dp2[i], dp2[i - C])
    if i >= D:
        dp2[i] = max(dp2[i], dp2[i - D])
sugerlist = []
for i in range(3001):
    if dp2[i] > 0:
        sugerlist.append(i)

ans = [0, 0]
concent = 0

for water in waterlist[1:]:
    if 100 * water <= F:
        left = F - (water * 100)
        # Fから水をひいた分、溶ける砂糖の限界を超えない量の砂糖を取得する
        index = bisect_right(sugerlist, min(left, E * water))
        suger = sugerlist[index - 1]
        # 濃度計算
        optconc = (100 * suger) / (100 * water + suger)
        # ここ>にすると濃度0%に対応できずWAに
        if optconc >= concent:
            concent = optconc
            ans = [100 * water + suger, suger]
print(*ans)

# ABC082 D - FT Robot
# grid dpの亜種
# dpx + x, dpx - xを収納していく

s = input()
x, y = map(int, input().split())

dpx = {0}
dpy = {0}

f = s.split("T")

fx = []
fy = []

for i, fi in enumerate(f):
    if i % 2:
        fy.append(len(fi))
    else:
        fx.append(len(fi))

for i, fxi in enumerate(fx):
    nex = set([])
    for j in dpx:
        nex.add(j+fxi)
        if i > 0:
            nex.add(j-fxi)
    dpx = nex

for fyi in fy:
    nex = set([])
    for j in dpy:
        nex.add(j+fyi)
        nex.add(j-fyi)
    dpy = nex

print(dpx)
print(dpy)

if x in dpx and y in dpy:
    print('Yes')
else:
    print('No')

# ABC113 D - Number of Amidakuji
H, W, K = getNM()

if W == 1:
    print(1)
    exit()

# 左からi本目の右、左に橋がかかっている通り、両方に通ってない通り
bridge_right = [0] * W
bridge_left = [0] * W
not_bridge = [0] * W

for bit in range(1 << (W - 1)):
    flag = True
    for i in range(1, (W - 1)):
        if bit & (1 << i) and bit & (1 << (i - 1)):
            flag = False
    if flag:
        for i in range(W):
            if i == 0:
                if bit & (1 << i):
                    bridge_right[i] += 1
                else:
                    not_bridge[i] += 1
            elif i == W - 1:
                if bit & (1 << (i - 1)):
                    bridge_left[i] += 1
                else:
                    not_bridge[i] += 1
            else:
                if bit & (1 << i):
                    bridge_right[i] += 1
                elif bit & (1 << (i - 1)):
                    bridge_left[i] += 1
                else:
                    not_bridge[i] += 1

dp = [[0] * W for i in range(H + 1)]

dp[0][0] = 1
for i in range(1, W):
    dp[0][i] = 0

# まっすぐ降りて来た場合、右から降りてきた場合、左から降りてきた場合
for i in range(1, H + 1):
    for j in range(W):
        dp[i][j] += dp[i - 1][j] * not_bridge[j]
        if j == 0:
            dp[i][j + 1] += dp[i - 1][j] * bridge_right[j]
        elif j == W - 1:
            dp[i][j - 1] += dp[i - 1][j] * bridge_left[j]
        else:
            dp[i][j + 1] += dp[i - 1][j] * bridge_right[j]
            dp[i][j - 1] += dp[i - 1][j] * bridge_left[j]

print(dp[-1][K - 1] % mod)

# ABC118 D - Match Matching
# まず長さを知りたい
# dp[i]: マッチN本までに最大何桁の数字ができるか
# その後、数字を上から回していって各桁の数字を確定させる
num = [2, 5, 5, 4, 5, 6, 3, 7, 6]

N, M = getNM()
A = getList()

digit = []
for i in A:
    digit.append([i, num[i - 1]])
digit.sort(key = lambda i: i[1])

dp = [-float('inf')] * (N + 1)
dp[0] = 0

# 桁数を調べる
for i in range(1, N + 1):
    for j in range(M):
        if i >= digit[j][1]:
            dp[i] = max(dp[i], dp[i - digit[j][1]] + 1)

# 数字を組み上げる
ans = ''
now = N
digit.sort(reverse = True)
while now > 0:
    for j in range(M):
        if now - digit[j][1] >= 0 and dp[now] == dp[now - digit[j][1]] + 1:
            now -= digit[j][1]
            ans += str(digit[j][0])
            break
print(ans)

# ABC130 E - Common Subsequence

"""
何通りあるでしょうか dpだ
N = M の場合を考える
1 3
3 1　の場合
1文字目 1, 3
()のみヒット
2文字目 3, 1
両方1, 両方3がヒット　これを()に加え
(1), (3)で合計3
dpを書いてみる
dp = [[0] * (M + 1) for i in range(N + 1)]
dp[0][0] = 1
[
[1, 1, 1],
[1, 1, ②],
[1, ②, 3]
]
N = 0の時
M = 0: 1 ()のみ
M = 1: 1 同上
M = 2: 1 同上

N = 1の時
M = 0: 1 () のみ
M = 1: 1 同上
M = 2: 2 1がヒットする

N = 2の時
M = 0: 1
M = 1: 2 3がヒットする
M = 2: 3 1がヒット

dp[i][j]に関係ありそうなのはdp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]
dp[2][2]の時dp[1][2]から何かしら受け継いでいるはず でないと1がマッチしてるのを引き継げない

S[i] == T[j]とS[i] != T[j]とで事情が分かれる
N = 1, M = 2の時、dp[0][2], dp[1][1]の時より場合が増える
dp[2][1]からdp[2][2]にいく時、dp[1][2]から状態を引き継いでいる
dp[i][j] = dp[i][j - 1]での増分 + dp[i - 1][j - 1]での増分 + dp[i - 1][j - 1]
dp[1][2]とdp[2][1]はdp[1][1]でマッチしてる分についてダブっている
何もないS[i] != T[j]の時　dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

S[i] == T[j]の場合、
1 1
1 1 の時dpは
[1, 1, 1]
[1, 2, 3]
[1, 3, 6]
dp[i - 1][j - 1]の通りにS[i] == T[j]となった分を後ろに足す
S[i] != T[j]の場合よりdp[i - 1][j - 1]だけ増え dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
"""

N, M = getNM()
S = getList()
T = getList()

dp = [[0] * (M + 1) for i in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = 1
for i in range(M + 1):
    dp[0][i] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if S[i - 1] == T[j - 1]:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            dp[i][j] %= mod
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
            dp[i][j] %= mod

print(dp[N][M] % mod)

# payment

N = input()
N = [int(i) for i in N]
# 数え上げ問題なので多分dp
dp = [[0, 0] for i in range(len(N))]

# ぴったし払うための最小値
dp[0][0] = min(N[0], 11 - N[0])
# お釣りをもらう用の紙幣を１枚余分にとっておく場合の最小値
dp[0][1] = min(N[0] + 1, 10 - N[0])

for i in range(1, len(N)):
    # dp[i - 1][1] + 10 - N[i]:とっておいた紙幣を使用し、お釣りを10 - N[i]枚もらう
    dp[i][0] = min(dp[i - 1][0] + N[i], dp[i - 1][1] + 10 - N[i])
    # dp[i - 1][1] + 9 - N[i]:お釣りを10 - N[i]枚もらい、そのうち１枚は次のお釣りを
    # もらう試行のためにとっておく
    dp[i][1] = min(dp[i - 1][0] + N[i] + 1, dp[i - 1][1] + 9 - N[i])
print(dp[len(N) - 1][0])

# ABC155 E - Payment
N = input()
N = [int(i) for i in N]
# 数え上げ問題なので多分dp
dp = [[0, 0] for i in range(len(N))]

# ぴったし払うための最小値
dp[0][0] = min(N[0], 11 - N[0])
# お釣りをもらう用の紙幣を１枚余分にとっておく場合の最小値
dp[0][1] = min(N[0] + 1, 10 - N[0])

for i in range(1, len(N)):
    # dp[i - 1][1] + 10 - N[i]:とっておいた紙幣を使用し、お釣りを10 - N[i]枚もらう
    dp[i][0] = min(dp[i - 1][0] + N[i], dp[i - 1][1] + 10 - N[i])
    # dp[i - 1][1] + 9 - N[i]:お釣りを10 - N[i]枚もらい、そのうち１枚は次のお釣りを
    # もらう試行のためにとっておく
    dp[i][1] = min(dp[i - 1][0] + N[i] + 1, dp[i - 1][1] + 9 - N[i])
print(dp[len(N) - 1][0])

# AGC031 B - Reversi

"""
通りの数はdpかcombo
0回以上する
最終的に全部同じになるのでは
小さいものから試す
1 2 1 2 2

1 2 1 2 2
1 1 1 2 2
1 2 2 2 2 間に異なる数字が入ってないといけない
nC2するっぽい
一度l ~ rを選ぶと、その区間内についてはもう使用不可
一つとして扱える

1 2 1 2 2 は
1 2 2 や
1 2 2 になる　この潰し方の通り
前から見ていくと
1 1通り
1 2 1通り
1 2 1 2通り
1 2 1 2 3通り
1 2 1 2 2 3通り
同じ数字が出ると？ 同じ数字が連続するのは圧縮する

1 3 1 2 3 2

1 3 1 2 3 2
1 1 1 2 3 2
1 3 3 3 3 2
1 3 1 2 2 2
1 1 1 2 2 2 前回のdpを足す
前回の数字に戻ると同じ圧縮列で異なる場合を作れる

1 3 1 と 1 3 1 1 1(変化させたやつ)は異なるが、
圧縮列1 3 1で同じ　この先同じように変化していく
"""

N = getN()
C = getArray(N)
C = [C[i] for i in range(N) if i == 0 or C[i] != C[i - 1]]
N = len(C)

table = [-1] * (2 * 10 ** 5 + 7)
dp = [0] * N
dp[0] = 1
table[C[0]] = 0

for i in range(1, N):
    dp[i] += dp[i - 1]
    if table[C[i]] >= 0: # 前回の部分があれば
        dp[i] += dp[table[C[i]]] # 前回の場所の分も足す
    table[C[i]] = i # 更新
    dp[i] %= mod

print(dp[-1] % mod)


# ACLB D - Flat Subsequence
# 実家DP
# Aの要素そのものに着目する(BITで大きい要素から置いていく感覚)
N, K = getNM()
A = getArray(N)
ma = max(A)

# Aの部分列
# Bの隣り合う要素の絶対値がK以下

# NlogNまでいける
# セグ木？ dp?
# 全てにエッジを貼る必要はない？
# LIS?
# まあdp

# 数字iの最長はなんぼか
seg = SegTree([0] * (ma + 1), segfunc, ide_ele)
dp = [1] * N
for i in range(N):
    dp[i] = seg.query(max(0, A[i] - K), min(ma, A[i] + K) + 1) + 1
    seg.update(A[i], dp[i])
print(max(dp))
