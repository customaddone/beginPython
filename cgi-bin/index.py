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
N, M = getNM()
F = getArray(N)

# 何通り　→ comb or dp
# O(N)で
# 同じ味のサプリメントを摂取しない
# dp[i]:i日目までにサプリを摂取する通りが何通りあるか
# dp[i]:サプリi個目までにサプリを摂取する通りが何通りあるか

# N, M = 5, 2
# L = [1, 2, 1, 2, 2]の場合
# dp[0] = 1
# dp[1] = 1 1個目を新たに食べた場合、それ以前の通りは1通り
# dp[2] = 2 2個目を新たに食べた場合、それ以前の通りは2通り
# (前回1個目を食べたかもしれないし、今回1個目と合わせて2個目を食べたかもしれない)
# dp[i] += dp[（最後にF[i]が登場した場所）] ~ dp[i - 1]

dp = [0] * (N + 1) # dpだけ1-index
dp[0] = 1
ignore = [0] * (M + 1)
l = 0
now = dp[0]
for r in range(N):
    # 最初ignoreのフラグが立っていないが,nowにはdp[0]の値が入っている状態
    while ignore[F[r]]:
        ignore[F[l]] = 0 # F[l]のフラグを消す
        now -= dp[l] # lの直前のdpを引く
        now %= mod
        l += 1
    # dpをレコード（範囲の合計を足す）
    dp[r + 1] = now
    # rを1個ずらして更新
    now += dp[r + 1]
    now %= mod
    ignore[F[r]] = 1

print(dp)

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
N, M = getNM()
S = getList()
N_s = len(S)
T = getList()
N_t = len(T)

dp = [[0] * (N_s + 1) for i in range(N_t + 1)]
dp[0][0] = 0

for i in range(N_t):
    for j in range(N_s):
        # 基礎 dp[i][j] + Sを伸ばして増えた分 + Tを伸ばして増えた分
        dp[i + 1][j + 1] = (dp[i + 1][j] + dp[i][j + 1] - dp[i][j]) % mod
        if S[j] == T[i]:
            # dp[i][j]の通りのそれぞれの末尾に(S[i], T[i])をつけることで
            # dp[i][j]通り（と空に(S[i], T[i])をつけた）分新しいのが作れる
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j] + 1) % mod
print((dp[N_t][N_s] + 1) % mod)

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
import heapq
import math
from fractions import gcd
import random
import string
import copy
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

N = getN()
C = getArray(N)
"""
違う場所の組み合わせを選んでも状態がダブル場合がある
[1, 2, 1, 2, 2]で2, 4番目を選ぶ場合と2, 5番目を選ぶ場合
ダブルのは含めないか、あとで引くか
要素2について
全く選ばない場合, (a, b)を選ぶ場合...
島にして考える
[1, 3, 1, 2, 3, 2, 1]の場合
区間(0, 2), (0, 6), (1, 4), (3, 5)を選べる
区間をピックアップするのは無理そう
ダブらないように区間を選びたい
最大流でできる？
ソートすると？
dpっぽい
"""

alta = []
for i in range(N):
    if i == 0 or C[i] != C[i - 1]:
        alta.append(C[i])
N = len(alta)

dict = defaultdict(list)
for i in range(N):
    dict[alta[i]].append(i)

dp = [0] * (N + 1)
dp[0] = 1
for i in range(N):
    # alta[i]を使わない場合
    dp[i + 1] += dp[i]
    # alta[i]を使う場合
    # alta[i]が最後に登場した位置をsとすると
    # s ~ alta[i]を使う、もしくはalta[i]を区間延長したパターンが使われる
    index = bisect_left(dict[alta[i]], i)
    if index > 0:
        dp[i + 1] += dp[dict[alta[i]][index - 1] + 1]
    dp[i + 1] %= mod
print(dp[N] % mod)

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
