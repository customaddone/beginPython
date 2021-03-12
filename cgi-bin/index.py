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

# JOI本戦 B - IOI饅頭（IOI Manju）
M, N = getNM() # M:饅頭 N:箱
sweets = getArray(M)
box = [getList() for i in range(N)] # 最大C個, E円　1個ずつ
# 菓子の価格 - 箱の価格 の最大値
# M <= 10000, N <= 500
# dp?

sweets.sort(reverse = True)
imos = [0]
for i in range(M):
    imos.append(imos[i] + sweets[i])

# 箱に詰める饅頭の価格を大きく、箱の価格を小さくする
# 合計でi個詰められる箱を用意した時の箱の価格の最小値
# 貪欲に前から?
# grid dp無理め? M <= 10000なのでそこまで求めるだけでいい
# 500 * 10000
prev = [float('inf')] * 10001
prev[0] = 0

for c, e in box:
    for j in range(10000, -1, -1): # 逆順に
        if j - c >= 0:
            prev[j] = min(prev[j], prev[j - c] + e)
        else:
            prev[j] = min(prev[j], prev[0] + e)

ans = 0
for i in range(1, M + 1):
    ans = max(ans, imos[i] - prev[i])
print(ans)

# JOI11予選 D - パスタ (Pasta)
N, K = getNM()
pasta = [[] for i in range(N)]
for i in range(K):
    a, b = getNM()
    pasta[a - 1].append(b - 1)

# 通りの数を求める: dp, 数え上げ組み合わせ
# n日前のことが関係する: n次元のdpを作れる

# modが10000
# パスタは3種類
# dp[j][k]: 本日jのパスタで、前日kのパスタの通り

prev = [[0] * 3 for i in range(3)]
# 1日目
if pasta[0]:
    prev[pasta[0][0]][(pasta[0][0] + 1) % 3] = 1
else:
    for i in range(3):
        prev[i][(i + 1) % 3] = 1

# 2日目以降
for p in pasta[1:]:
    next = [[0] * 3 for i in range(3)]
    # すでに決められているなら
    if p:
        j = p[0]
        # 本日のパスタjは確定
        # その前の日のパスタnext[]j[k]のk, prev[j][k]のjは3通り
        # そのまた前日のパスタprev[j][k]のkは3通り
        for k in range(3):
            for p_k in range(3):
                if j == k and k == p_k:
                    continue
                next[j][k] += prev[k][p_k]
                next[j][k] %= 10000
    else:
        for j in range(3):
            for k in range(3):
                for p_k in range(3):
                    if j == k and k == p_k:
                        continue
                    next[j][k] += prev[k][p_k]
                    next[j][k] %= 10000
    prev = next

ans = 0
for i in range(3):
    for j in range(3):
        ans += prev[i][j]
        ans %= 10000
print(ans)

# Code Formula 2014 本選 D - 映画の連続視聴

"""
N <= 3000 O(N ** 2)まで
Mの映画が[S ~ E]までの間上映されている
同じ映画を見ることでより多くの幸福感
違う映画を見るとリセットされる
上映時刻がダブってなければ連続して視聴可能

まず貪欲を考える
区間スケジューリング
終わりの時刻でソート
[[2, 10, 40], [1, 0, 120], [1, 15, 135], [1, 240, 330]]
どの映画を１回見ても幸福度は同じ　出来るだけ連続させた方がいい？
連続してみると幸福度は絶対上がる
全探索？
同じ映画を見た場合、違う映画を見た場合
S, Eが小さいのでDPできそうO(N ** 2)できるので
同じ種類のものは連結して考えられる
1: [1, 0, 120], [1, 15, 135], [1, 240, 330]
2:    [2, 10, 40]
[2, 10, 40]をとる　次取れるのは[1, 240, 330]
[2, 10, 40]をとらない
2 → 3と繋いで100しか上がらなくでも、3 → 4とつなぐと100000上がるかもしれない
streak1: 何個
streak2: 何個..という風に数える
合成して区間スケジューリングかも
3 + 2がバッティングしても2 + 2なら通るかもしれない
2 + 2より3 + 1の方が強い
MAX連続を想定する

### 今いくつ連続してるかを考えなくていいようにする ###
1つ連続させたもの、2つ連続させたもの...をmovieに混ぜ込む
セグ木を使う
合成したものを混ぜ込む
"""

N = getN()
H = getList()
for i in  range(N - 1):
    H[i + 1] += H[i]
movie = [getList() for i in range(N)]
movie.sort(key = lambda i: i[2])

# セグ木を使わないver
dp = [0] * (10 ** 5 + 7)
prev = 0
for i in range(N):
    m, s, e = movie[i]
    # 初期化
    for j in range(prev + 1, e + 1):
        dp[j] = max(dp[j], dp[j - 1])
    prev = e

    dp[e] = max(dp[e], dp[s] + H[0])
    cnt = 0

    # 現在のtargetから区間スケジューリング
    for j in range(i + 1, N):
        nm, ns, ne = movie[j]
        if nm != m:
            continue
        if e <= ns:
            cnt += 1
            e = ne
            dp[e] = max(dp[e], dp[s] + H[cnt])

print(max(dp))

# みんなのプロコン2019 D - Ears

"""
必要な回数の最小値　効率的な方法を考える
散歩開始と終了地点は任意

0 ○ 1 ○ 2 ○ 3 ○ 4
地点iを
前方向に i += 1
後方向に i-1 += 1

出発の回数はsum(A)
diffの最小値を目指す　二分探索したい

1 - 2の周回で無限に地点2の石を増やせる
ただし偶奇によって状況は変わる
0が多い場合は避けるといいぞ
範囲内は確実に1は増える
L <= 10 ** 5
偶奇または0の累積
セグ木も使える

(ゼロゾーン)(偶数ゾーン)(奇数ゾーン)(偶数ゾーン)(ゼロゾーン)
両端の偶数ゾーンはなくてもいい
0の処理は
LC2でもダメ
区切りは1つだけ 累積してみる
任意のゼロゾーンを

独立してゾーンを考えられるはず
まず奇数ゾーンを置く

偶数ゾーン2つがそれぞれ存在する場合、しない場合を考える
ゼロも偶数として考えるか

奇数の方がいい区間
中央で分ける
それぞれ
(ゼロゾーン)(偶数ゾーン)
左側の最小コスト + 右側の最小コスト
セグ木使えば

マーブルと同じようにDP
"""

L = getN()
A = getArray(L)

dp = [[0] * (L + 1) for _ in range(5)]

for i in range(L):
    if A[i] == 0: # 0のとこに突入するなら
        t = 2
    else:
        t = A[i] % 2
    # それぞれ前の状態から遷移できる
    dp[0][i + 1] = dp[0][i] + A[i]
    dp[1][i + 1] = min(dp[0][i + 1], dp[1][i] + t)
    dp[2][i + 1] = min(dp[1][i + 1], dp[2][i] + (A[i] + 1) % 2)
    dp[3][i + 1] = min(dp[2][i + 1], dp[3][i] + t)
    dp[4][i + 1] = min(dp[3][i + 1], dp[4][i] + A[i])

print(dp[4][L])

# EDPC j - shshi

"""
dp[i][j][k]: i個、j個、k個ある時全部なくすための期待値
N <= 300 O(N ** 3)まで
dp[i][j][k] = i / N * dp[i - 1][j][k] + j / N * dp[i][j - 1][k]
+ k / N * dp[i][j][k - 1] + (N - i - j - k) / N * dp[i][j][k]
dp[i][j][k]をまとめると
dp[i][j][k] = (i * dp[i - 1][j][k] + j * dp[i][j - 1][k] + k * dp[i][j][k - 1] + N) / (i + j + k)
"""

N = getN()
A = getList()
c = Counter(A)
a, b, c = c[1], c[2], c[3]
dp = [[[0] * (N + 2) for i in range(N + 2)] for j in range(N + 2)]

for i in range(c + 1): # 上限はc
    for j in range(N - a - i + 1): # 上限はb + c
        for k in range(N - i - j + 1):
            if i + j + k:
                dp[i][j][k] = (i * dp[i - 1][j + 1][k] + j * dp[i][j - 1][k + 1] + k * dp[i][j][k - 1] + N) / (i + j + k)

print(dp[c][b][a])

# CODE THANKS FESTIVAL 2018(Parallel) E-union

"""
指数関数的なdp遷移
ただ一つだけの整数が黒板にある状態
数字iが0 ~ i個置ける A1 * A2 * ... に見える
条件:同じ数字を２つ消してX+1を一個書くを繰り返すと最終的に整数1つになるように
整数の置き方は何通りあるか　遷移の方法を考える

3
2 1 1の場合

例えば1: 1個とか2: 1個とか
1: 2個の場合は2: 1個にできるのでok
1: 2個, 2: 1個の場合は3: 1個にできるのでok
制約的にdpできそう　dp[i][j]:
3が1個, 3が2個, 3が4個　これらは条件を満たす

"""

T = getN()
A = getList()
dp = [[0] * 1000 for i in range(T)]
for i in range(A[0] + 1):
    dp[0][i] += 1

ans = dp[0][1]
for i in range(1, T):
    # 前回の0のもの、2のもの、4のもの...
    for j in range(0, 1000, 2): # i - 1から持ってくるもの
        for k in range(A[i] + 1): # iで生成するもの
            dp[i][k + (j // 2)] += dp[i - 1][j]
            dp[i][k + (j // 2)] %= mod
    ans += dp[i][1]
    ans %= mod

for i in range(1, 10):
    ans += dp[-1][1 << i]
    ans %= mod
print(ans % mod)

# Tenka1 Programmer Beginner Contest 2019
# D Three colors

"""
300個の整数を赤、青、黄の3色で塗る
それぞれの総和についてsum(r, g, b) - 2 * max(r, g, b) > 0
sum(r, g, b) > 2 * max(r, g, b)となる組み合わせはいくつ存在するか
愚直にやれば3 ** N

dpっぽいが？
max(r, g, b)の候補を作成し(iとする)それにrgbどれか一色を塗る
それが最大かつi < sum - i でないといけない

dpをすると
総和がjになる通りがl通りある　がわかる
総和がjになる　はわかってもどの要素を使っているかはわからない

耳dpとか？
[1, 1, 1, 2]の時、もっとも大きい辺は2でないといけない
ダブりまくるが
dp[i][j][l]: i個目まで進んだ時、赤の合計がiかつ青の合計がj
のdpなら一瞬で答えが出るが　遷移方法は
多分無理

あらかじめ赤のを控除しとく　これとこれとこれを控除した時
あまりので青を作る通りがこれだけある　残りは黄色

N = getN()
A = getArray(N)
su = sum(A)

dp = [0] * (su + 1)
dp[0] = 1
for i in range(N):
    for j in range(su, -1, -1):
        if j + A[i] <= su:
            dp[j + A[i]] += dp[j]
print(dp)
まずグループを２つに分ける操作において
dp[i]とdp[sum - i]はリンクする
[1, 1, 1, 2]のとき
dp = [1, 3, 4, 4, 3, 1] 左右対称
dp[2] = dp[4] = 4
dp[2]のどれかの通りがdp[4]のどれかの通りに対応する
dp[2]のどれかの構成に基づいてAから数字を取り除く

3 ** Nから条件を満たさないものを消す
赤が1/2を超えない場合は、青、黄色が存在しない2通り
赤が1/2以上の場合は全ての場合で存在しない
N = getN()
A = getArray(N)
su = sum(A)

prev = [0] * (su + 1)
prev[0] = 1
for i in range(N):
    next = [0] * (su + 1)
    for j in range(su + 1):
        # 赤で塗る
        if j + A[i] < su + 1:
            next[j + A[i]] += prev[j]
        # 青で塗る
        next[j] += prev[j]
        # 黄で塗る
        next[j] += prev[j]
    prev = next

print(sum(prev[(su + 1) // 2:]))
"""

N = getN()
A = getArray(N)
su = sum(A)

# mainになるdp
prev = [0] * (su + 1)
prev[0] = 1
for i in range(N):
    next = [0] * (su + 1)
    for j in range(su + 1):
        # 赤で塗る
        if j + A[i] < su + 1:
            next[j + A[i]] += prev[j]
            next[j + A[i]] %= mod
        # 青で塗る
        next[j] += prev[j]
        next[j] %= mod
        # 黄で塗る
        next[j] += prev[j]
        next[j] %= mod

    prev = next

diff = sum(prev[(su + 1) // 2:])

# もしsu % 2 == 0なら真っ二つに分割でき、ダブりが生まれる
if su % 2 == 0:
    dp = [0] * (su + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(su, -1, -1):
            if j + A[i] <= su:
                dp[j + A[i]] += dp[j]
                dp[j + A[i]] %= mod
    diff -= dp[(su + 1) // 2]

print((pow(3, N, mod) - 3 * diff) % mod)

# エクサウィザーズ2019 D - Modulo Operations

N, X = getNM()
S = getList()

S.sort()

# XがS[i]より大きい場合にXが小さくなる
prev = [0] * (X + 1)
prev[X] = 1

# Sを逆から見ていく
for i in range(N - 1, -1, -1):
    next = [0] * (X + 1)
    # 5 82
    # 22 11 6 5 13 の場合
    # それぞれを操作列として採用するか
    for j in range(X + 1):
        prev[j] %= mod
        # 採用しない場合
        # 今までの数列のうち先頭以外に挿入する この通りがi通り
        next[j] += prev[j] * i % mod
        # 採用する場合
        next[j % S[i]] += prev[j]
    prev = next

print(sum(i * prev[i] % mod for i in range(S[0])) % mod)
