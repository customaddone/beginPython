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
# sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# ABC144 F - Fork in the Road

"""
塞いだあと高橋くんがどこかで詰まったらだめ
辺を一つ消す　判定するをN回繰り返す
dpする？
dp[i][j]: 頂点iにj回の移動で到達する確率

# dp[i][j]: 頂点iにj回の移動で到達する確率
dp = [[0] * (N + 1) for i in range(N)]
dp[0][0] = 1

# 頂点
for i in range(N):
    # j回の移動で
    for j in range(i + 1):
        for v in E[i]:
            dp[v][j + 1] += dp[i][j] / len(E[i])
print(dp)

一回の判定でO(M)ぐらいかかる
エッジにウェートをかけると？
エッジを見るだけでなんとかなるように
dpの全てについて調べる必要はないんでは
P[s] * (1 / M)の大きさが最も大きいものが一番Nの期待値への寄与度が大きい
"""

N, M = getNM()
dist = [[] for i in range(N)]
for i in range(M):
    s, t = getNM()
    dist[s - 1].append(t - 1)
for i in range(N):
    dist[i].sort()

# トポロジカルソートにすればs < tの条件がなくても使える
def calc(edges):
    # 確率を計算
    P = [0] * N
    P[0] = 1
    for u in range(N):
        for v in edges[u]:
            P[v] += P[u] / len(edges[u])

    # 期待値を計算　ゴールから逆向きで期待値を求める
    # あと何回進めばゴールまで行けるか
    E = [0] * N
    for u in range(N - 1, -1, -1):
        for v in edges[u]:
            # この(E[v] + 1)が大きくなるものを削ればいい
            E[u] += (E[v] + 1) / len(edges[u])

    return P, E

P, E = calc(dist)
ans = E[0]
diff = 0

for u in range(N):
    for v in dist[u]:
        if len(dist[u]) > 1:
            # u ~ vの辺を削ると(E[v] + 1) / len(dist[u])の分だけ軽くなるが
            # 残った分が len(dist[u]) / (len(dist[u]) - 1)でかけられる
            ban = (E[v] + 1) / len(dist[u]) # これが消える予定
            new = (E[u] - ban) * len(dist[u]) / (len(dist[u]) - 1)
            diff = max(diff, (E[u] - new) * P[u])

print(ans - diff)

# M-SOLUTION プロコン　C - Best-of-(2n-1)

"""
数学問題でーす
どちらかが累計でN回勝てば良い　遷移を考える N^2解から考える
高橋くんが1回勝って終わる確率
答えは整数 / 整数になるらしい

高橋くんがN回勝って終わる時
青木くんはN - 1回以下の任意の整数回勝って終わっている
青木くんが勝つ確率をb回で固定して足し合わせ
引き分けは無限回あって良い
青木くんがN回勝って終わるのは逆になる
２つは独立事象か？

N+b+cCc * N+bCb * (A / 100)^N * (B / 100)^b * (C / 100)^c

期待値を計算
dp[1][0] = A / 100 * (dp[0][0] + 1) + C / 100 * (dp[1][0] + 1)
dp[i][j] = A / 100 * (dp[i - 1][j] + 1) + B / 100 * (dp[i][j - 1] + 1) + C / 100 * (dp[i][j])
(100 - C)dp[i][j] = A * (dp[i - 1][j] + 1) + B * (dp[i][j - 1] + 1)

合計でN回勝つ期待値でdpとるか
dp[i]: どちらかがN回勝って終わっている
i+1だと？

一発では無理
ans += 期待値 / 確率を全ての場合で求めるやり方

確率の求め方
高橋くんがa回、青木くんがb回出すとすれば
a+bCa * (A / A + B)^a * (B / A + B)^b
a+bCa * A^a * B^b * (A + B)^a+b
高橋くんがN回、青木くんが0回、1回...その逆を求めるなら

高橋くんがN-1回、青木くんがi回勝ち、さらに高橋くんが勝てば良い

高橋くんがN回、青木くんがi回勝つのにかかる期待値
マスを一つ移動するのにかかる期待値は？
C = 0なら自明にa + bになる
100 * (N + i) / 100 - C
100 / 100 - Cは空回り分

A == B == 0はない
"""

# 逆元事前処理ver
# nが小さい場合に
lim = 10 ** 6 + 1
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

N, A, B, C = getNM()
a_pow = [1] * (10 ** 6 + 1)
b_pow = [1] * (10 ** 6 + 1)
for i in range(1, 10 ** 6 + 1):
    a_pow[i] = (a_pow[i - 1] * A) % mod
    b_pow[i] = (b_pow[i - 1] * B) % mod

ans = 0
# 高橋くんがN-1回、青木くんが0 ~ N - 1回勝ったあと、高橋くんが勝つ

for i in range(N):
    # 分子はpowして良い
    prob = ((cmb(N + i - 1, i) * a_pow[N - 1] * b_pow[i]) * A) % mod
    # 分母は(A + B) ** (2 * N - 1)に揃える
    prob *= pow(A + B, N - i - 1, mod)
    prob %= mod
    # deno = (A + B) ** (2 * N - 1)

    # 期待値　分子部分
    exp = 100 * (N + i)
    # 分母はA + B
    ans += prob * exp
    ans %= mod

# 青木くんサイド
for i in range(N):
    prob = ((cmb(N + i - 1, i) * a_pow[i] * b_pow[N - 1]) * B) % mod
    prob *= pow(A + B, N - i - 1, mod)
    prob %= mod

    exp = 100 * (N + i)
    ans += prob * exp
    ans %= mod

# 最後に確率計算(A + B) ** (2 * N - 1)、期待値(A + B)
# 計((A + B) ** (2 * N))で割ることにする
# 分母の逆元の計算はこうやる
deno = (pow(A + B, 2 * N, mod)) % mod
print((ans * pow(deno, mod - 2, mod)) % mod)

# ARC106 D-power

"""
掛け算をする
N(N - 1) // 2個全てを計算するのは無理
天才式変換をしよう
(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3
a1, a2...が出る回数はそれぞれ(N - 1)回
a^3, b^3部分のsumはすぐでる
あらゆるa^2bのsumを求めたい
1^2 * 2^1 + 1^1 * 2^2
1^2 * 3^1 + 1^1 * 3^2
2^2 * 3^1 + 2^1 * 3^2
1^1の相手は2^2, 3^2
一般化すると
k乗する場合
0-indexでの第i項目、第k - i項目のことを考える
kCiをあとでかける
ai^iの相手は(任意のaj^k-i)
ai^k-iの相手は(任意のaj^i)
これのsumは
1 0 1
2 0 2 真ん中が抜ける
3 0 3
3 1 2
[[1, 1, 1], [1, 2, 3], [1, 4, 9], [1, 8, 27]]
[3, 6, 14, 36]
ここで72
1^0の相手は36 - 1 = 35
2^0の相手は36 - 8 = 28
3^0の相手は36 - 27 = 9 これらは3C0でかける
ここで144
1^1の相手は2^2 + 3^2 = 14 - 1^2 = 13
2^1の相手は14 - 4 = 10
3^1の相手は14 - 9 = 5 これらは3C1でかける　合計216

まとめたいが
su_p[i] * su_p[x - i] - (p_l[i][n] * p_l[x - i][n]の合計)
(p_l[i][n] * p_l[x - i][n]の合計)はsu_p[x]で一定
kCi * (su_p[i] * su_p[x - i] - su_p[x])

0-indexでの第i項目、第k - i項目のことを考えると
a^i * b^k-iは合計でN(N - 1)//2個ある
a^k-i * b^iも合計でN(N - 1)//2個ある
その合計は(各Aをi乗した値の合計) * (各Aをk-i乗した値の合計) - (各Aについて^i * ^k-i = k乗した値の合計)
これらに係数kCiをかける
"""

N, K = getNM()
A = getList()

p_l = [[0] * N for i in range(K + 1)]
for i in range(K + 1):
    for j in range(N):
        if i == 0:
            p_l[i][j] = 1
        else:
            p_l[i][j] = (p_l[i - 1][j] * A[j]) % mod

su_p = [sum(p_l[i]) % mod for i in range(K + 1)]

for x in range(1, K + 1):
    ans = 0
    for i in range(x + 1):
        ans += cmb(x, i) * (su_p[i] * su_p[x - i] - su_p[x])
        ans %= mod
    print((ans * pow(2, mod - 2, mod)) % mod)

# ABC215 G - Colorful Candies 2 

"""
期待値: 全ての通りについて考える
この色が選ばれる通りの数について足し合わせ　→　この色が選ばれない通りの数の引き合わせも考えられる
一つも選ばれない場合の数を考える
全ての場合がnCk通りで、その全てについて

補集合を考える　期待値はこれが選ばれると += 1と考える
この色が選ばれない通りの数　を考える
これ以外のやつで構成する

for k in range(1, N + 1):
    deno = cmb(N, k)
    nume = (deno * len(d)) % mod
    # ここの計算が多い！
    for _, v in d.items():
        nume -= cmb(N - v, k)

    nume %= mod
    deno = pow(deno, mod - 2, mod)
    print((nume * deno) % mod)

cmb(N - v, k)で引くところをうまく計算する
kは1つずつ増えていくので...
"""

N = getN()
A = getList()
d = defaultdict(int)
for a in A:
    d[a] += 1
# 数字がi個ある数字が何個あるか
c = defaultdict(int)
for _, v in d.items():
    c[v] += 1

# nCk
for k in range(1, N + 1):
    deno = cmb(N, k)
    nume = (deno * len(d)) % mod # 全ての通りで全ての色を選べると仮定
    diff = []
    # n個ある数字がv種類ある
    for n, v in c.items():
        nume -= cmb(N - n, k) * v

    nume %= mod
    deno = pow(deno, mod - 2, mod)
    print((nume * deno) % mod)
