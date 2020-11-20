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

# キーエンス プログラミング コンテスト 2019 D - Double Landscape

"""
1 ~ N * M の整数を書き込む
i行目の数字の最大の数字はA
j行目の数字の最大の数字はB

反転数の数を求める時は列ごと入れ替え、列内入れ替えを行った
書き込みの個数を求めよ dpかcombo?

条件の満たし方を考える
まず条件を満たすものを一つ出す
Aiがn　i行目にはnとn以下の数字しか書かれていない

AとB両方に登場するとは限らない
ある数について指定の場所に置かないといけない
あとは自由 comboで求める
3 3
5 9 7
3 6 9
  5 9 7
3
6
9

9を置く
  5 9 7
3
6
9   9
8を置く　置けない！

二次元累積和？
N * M ~ 1まで１つずつ数を置いていく
iがAにある and Bにある
・解放する部分
今まで解放された部分と今回解放する部分の交わるとこ + 今回解放されるとこのクロス
・置けるとこ
1箇所　今回解放されるとこのクロス

iがAにある ^ Bにある
・解放する部分
今まで解放された部分と今回解放する部分の交わるとこ
・置けるとこ
今回解放されたとこのいずれかに置く

A,Bにない
現在解放されているマスのどこにでも置ける
"""

N, M = getNM()
A = set(getList())
B = set(getList())
if len(A) < N or len(B) < M: # A,B内で数字がダブってたら0
    print(0)
    exit()

ans = 1
opened = 0 # 解放されたマス
a_allowed = 0 # 解放された行
b_allowed = 0 # 解放された列

for i in range(N * M, 0, -1):
    if (i in A) and (i in B):
        # 解放はできる
        opened += (a_allowed + b_allowed) + 1 # 今まで解放された部分と今回解放する部分の交わるとこ + 今回解放されるとこのクロス
        a_allowed += 1
        b_allowed += 1
        opened -= 1 # 解放されたマスに置く
        # ans *= 1 # 置けるのは1箇所　今回解放されるとこのクロス
    elif (i in A):
        opened += b_allowed # 解放する行 * 解放されている列
        a_allowed += 1
        ans *= b_allowed # 今回解放された行のいずれかに置く
        opened -= 1
    elif (i in B):
        opened += a_allowed
        b_allowed += 1
        ans *= a_allowed
        opened -= 1
    else:
        ans *= opened # 解放されている部分のどこに置いても良い
        opened -= 1

    ans %= mod

print(ans)

# SoundHound Inc. Programming Contest 2018 -Masters Tournament- C - Ordinary Beauty

"""
差の絶対値がdであるものだけをピックアップ
合計でn ** m通り
期待値　通りの数は求めなくていい
m - 1の内1 ~ m - 1箇所について
1つめの数字 n通り
2つめの数字 n通りあるが、この内条件を満たす通りは
上向き　1つ目 1なら 1 + d
　　　　 　　 2なら 2 + d...(n - d)通り
            n - dなら n
下向きも同様に (n - d)通り
合計2 * (n - d)通り
つまりm - 1のうちの一つの谷間が条件を満たす確率は
2(n - d) / n ** 2
あとは美しさが1, 2...m - 1のものを足し合わせるだけ
comboすら必要ない？

足し合わせで求められる
1つ目が条件を満たす通り 2(n - d) / n ** 2 * (n ** M 全通り）足す
2つ目が条件を満たす通り 2(n - d) / n ** 2 * (n ** M 全通り）足す
1つ目が条件を満たす　と　2つ目が条件を満たす　は互いに独立
n - dが0になることもそうすれば求める値は0
またDが0なら上向き下向きではなく同じ値しか取れない
"""

N, M, D = getNM()
# (M - 1): 1 ~ M - 1まで足し合わせる
# 2 * (N - D): 2 * (N - D)) / (N ** 2) * (n ** M）を(n ** M）で割って平均値を出す
if D == 0:
    print((M - 1) * (max(0, N - D)) / (N ** 2))
else:
    print((M - 1) * 2 * (max(0, N - D)) / (N ** 2))

# AGC025 B - RGB Coloring

"""
数え上げcomboだろ
rgbなのでbitもある

ブロックが縦一列にあり、これを塗っていく
赤色: A点
緑色: A + B点
青色: B点
KはでかいがN, A, Bは小さい
塗らないブロックがあってもいい　→ 塗らないブロックが1個、2個...N個の場合

4 1 2 5 の場合
緑色1つ、青色1つ 4 * 3
赤色1つ、青色2つ 4 * 3
赤色2つ、緑色1つ 4 * 3
赤色3つ、青色1つ 4 * 1
の40通り
組み合わせを考えればいい

赤を固定すると 各O(1)で
赤0個, 赤1個, 赤2個...赤N個
緑の個数を決めれば青の個数も定まる　これだとO(N ** 2)
緑色: A + B点 が奇妙
緑色: 赤と青を同時に塗ると考えれば
A点加算されるブロックがi個(0 <= i <= N), B点加算されるブロックがj個
A点が0個、1個...N個の場合を調べる
4 1 2 5 の場合
A点: 0個　なし
A点: 1個(1点) B点は2個(4点)
A点: 2個(2点) なし
A点: 3個(3点) B点は1個(2点)
A点: 4個(4点) なし

A点に重ねて置いたB点（緑色になる）とそうでないB点は区別される

数え上げの問題は包除原理使ってダブったのを捨てたり
既に目標を達成した部分集合のcnt, まだ目標を達成してない部分集合とその達成度のcntを保持したり
今回のように分解して解いたりできる
"""

N, A, B, K = getNM()
ans = 0
# A点が0個、1個...N個の場合を調べる
for alpha in range(N + 1):
    if (K - (A * alpha)) % B != 0:
        continue
    beta = (K - (A * alpha)) // B
    ans += (cmb(N, alpha) * cmb(N, beta)) % mod
    ans %= mod

print(ans)

# ABC127 E - Cell Distance

"""
全ての場合　＝　全ての通りの数をまず考える
そのあと、ある事象が出現する確率を求める

全ての通りは nmCk
平均値の考え方　
つまりO(N + M)の足し合わせみたいな
ダブった奴は割ったり引いたりすればいい

2 2 2なら
4 * 3 // 2! = 6通り　順列分あとでわる
nCr通りある
この中でマスiとjが同時に出現する確率は　一定のはず
iとjが同時に出現するのはn-2Ck-2通り
iとjの選び方 nC2通り
コストiになるペアがいくつあるか
iとjのコスト * n-2Ck-2 をnC2通りやる
nC2通りのうちいくつがコストi
H - a * W - b コストa + b
コストのとり方は最大でもN + M - 2数え上げ

マンハッタン距離は上下と左右別々に求められる

こういう問題でコストiを何回足したらいいかを考えるのは鉄則
コストの規則性が分かりづらい　分けて考える
コストiを何回足したらいいかは難しそう　マスiについてのコストの総和を求めればいい

(1, 1)について
横方向のマンハッタン距離
距離1: 1 * H個
距離2: 1 * H個...
距離W - 1: 1 * H個
つまり(1, 1)についてコストの合計はW(W - 1) // 2 * H * (n-2Ck-2)
これを(1, 1) ~ (H, 1)までH回やる

(1, 2)について
距離1: 1 * H個
距離2: 1 * H個...
距離W - 2: 1 * H個
(1, 2)についてコストの合計は(W - 1)(W - 2) // 2 * H * (n-2Ck-2)
これを(1, 2) ~ (H, 2)までH回やる

これを縦方向のマンハッタン距離でもやる

巨大数のcmbをどうやる？
n-2Ck-2
"""

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

N, M, K = getNM()

ans = 0
for i in range(M - 1, 0, -1):
    ans += i * (i + 1) * (N ** 2) // 2
    ans %= mod

for i in range(N - 1, 0, -1):
    ans += i * (i + 1) * (M ** 2) // 2
    ans %= mod

print(ans * cmb(N * M - 2, K - 2) % mod)

# ABC168 E - ∙ (Bullet)

"""
美味しさA 香りB
一匹以上を入れる通りの数
そのままだと通りの数は2 ** N通り
ただし、かけ合わせると0になるものは一緒に入れられない
全て - NGの組み合わせを含むものもできる

Ai * Aj = -1 * Bi * Bj になるとだめ
マイナス逆数になるとだめ
M = defaultdict(int)
O = defaultdict(int)

for a, b in I:
    split = math.gcd(abs(a), abs(b))
    M[(a // split), (b // split)] += 1
    O[(a // split), (b // split)] += 1

for a, b in I:
    print(a, b)
    print(O[(-b, a)], O[(b, -a)])
個数でもつ
dictで持てるんでは

一緒にできないペアはわかった

1番目までを使い、1番目を含む通り 2 ** 0 = 1通り
2番目までを使い、2番目を含む通り 2 ** 1 = 2 通り
3番目までを使い、3番目を含む通り 1は一緒に使えないので0(使わない)固定
2 ** (2 - 1) = 2通り

これまでに弾かれた通りを保持しておく
10
3 2
3 2
-1 1
2 -1
-3 -9
-8 12
7 7
8 1
8 2
8 4

-8 12 が存在する通り 2 ** 5 = 32通り
そのうち32は登場しないようにするため2 ** (5 - 2) = 8通りのみ
3 2登場 1通り
3 2登場 前の3 2がある通り1通り + 無い通り1通り = 2通り

どちらかが0の場合がある

グループ組み合わせ掛け算
(2, 1)と(-1, 2)は同時に選べないのでペアにする
この時、(-1, 2)と(1, -2)は同値として扱う(1, 2, マイナス)とでもしとく
"""

N = getN()

d = defaultdict(int)
z = 0
for _ in range(N):
    a, b = getNM()
    if a == 0 and b == 0: # 後で足す
        z += 1
        continue
    # a == 0の場合は(0, 1)で登録
    if a == 0:
        b = 1
    if b == 0:
        a = 1
    if b < 0: # 強制的にbがプラスになるように
        a, b = -a, -b
    g = math.gcd(a, b)
    a //= g
    b //= g
    d[(a, b)] += 1

res = 1
seen = set()
for k in list(d):
    a, b = k
    if k in seen:
        continue

    # 掛けると0になる相手を作る
    if a < 0:
        x, y = b, -a
    else:
        x, y = -b, a
    if a == 0:
        x, y = 1, 0
    if b == 0:
        x, y = 0, 1

    # 計算
    res *= pow(2, d[(a, b)], mod) + pow(2, d[(x, y)], mod) - 1
    res %= mod
    # print(res)
    seen.add(k)
    seen.add((x,y))

res += z
res -= 1

print(res % mod)
