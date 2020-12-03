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

# ABC038 D-プレゼント
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def ope(self, x, y):
        return max(x, y)

    def update(self, i, v):
        j = i
        while j <= self.n:
            self.data[j] = self.ope(self.data[j], v)
            j += j & -j

    def query(self, i):
        ret = 0
        j = i
        while 0 < j:
            ret = self.ope(self.data[j], ret)
            j &= (j - 1)
        return ret

bit = BIT(10 ** 5)

for w, h in que:
    # 高さh未満の箱が何個あるか(wは昇順にソートしてるので考える必要なし)
    # 最初は0個
    q = bit.query(h - 1)
    # 高さhの時の箱の数を更新
    bit.update(h, q + 1)
print(bit.query(10 ** 5))

# ABC140 E - Second Sum
# [Pl, Pr]間で２番目に大きいものの総和を
# l, rについてのnC2通りの全てについて求めよ

# 8 2 7 3 4 5 6 1
# 8 2: 2
# 8 2 7: 7
# 2 7 3: 3
# 8を含むもの（７通り）について2が２番目になるもの、7が２番目になるもの...
# 2を含むものについて（６通り）について7が...をそれぞれO(1)で求められれば

# N <= 10 ** 5
# Piが２番目になる通りが何通り　みたいな感じで求められる？
# Piが２番目になる条件　→　自分より上位のものを一つだけ含む

# ヒープキューとか使える？
# 二つ数字を入れる　→　最小値を取り出せばそれは２番目の数字
# 尺取り使える？

# 累積？　一番

class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1

    def add(self, a, w):
        x = a
        while(x <= self.N):
            self.bit[x] += w
            x += x & -x

    def get(self, a):
        ret, x = 0, a - 1
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    def cum(self, l, r):
        return self.get(r) - self.get(l)

    def lowerbound(self,w):
        if w <= 0:
            return 0
        x = 0
        k = self.b
        while k > 0:
            if x + k <= self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x + 1

N = getN()
P = getList()
dic = {}
bit = BIT(N)
for i in range(N):
    dic[P[i]] = i + 1

# 両端に何もない時用
# [0] + Pの各要素 + [N + 1]みたいになる
dic[0] = 0
dic[N + 1] = N + 1
ans = 0

for i in range(N, 0, -1):
    # 8のインデックス、7のインデックス...に1を登録していく
    bit.add(dic[i], 1)
    # 左側にある既に登録したもの（自分より大きいもの + 自分）の数を数える
    c = bit.get(dic[i] + 1)
    # l1: 左側にある既に登録したもの（自分より大きいもの）のうち、一番右にあるもの
    # l2: l1の一つ左側にあるもの
    l1, l2 = bit.lowerbound(c - 1), bit.lowerbound(c - 2)
    # r1: 右側にある既に登録したもの（自分より大きいもの）のうち、一番左にあるもの
    # r2: r1の一つ右側にあるもの
    r1, r2 = bit.lowerbound(c + 1), bit.lowerbound(c + 2)
    S = (l1 - l2) * (r1 - dic[i]) + (r2 - r1) * (dic[i] - l1)
    ans += S * i
print(ans)

# ABC174 F - Range Set Query

# 色の種類
# 同じ色のボールがある場合、どの情報があれば良いか
# 最もrに近いボールの位置がわかればいい
N, Q = getNM()
C = [0] + getList() # 1-indexに
que = [[] for i in range(N + 1)]
for i in range(Q):
    l, r = getNM()
    que[r].append([l, i])

ans = [0] * Q # これだけ0-index
place = [-1] * (N + 1) # 一番右にあるボールの場所
bit = BIT(N + 1) # できるならbitに

# 前から更新していく
for r in range(1, N + 1):
    # 更新
    c = C[r]
    bit.add(r, 1) # 立てる
    if place[c] > 0: # 登録済みなら
        bit.add(place[c], -1)
    place[c] = r

    # 答える
    while que[r]:
        l, index = que[r].pop()
        ans[index] = bit.cum(l, r + 1)

for a in ans:
    print(a)

# ARC031 C - 積み木
"""
最小回数を求める
ヒストグラムは
A = {1, 2, 3...}について
Aiより左にある自分より小さいものの数　の総和
順番は小さい順に
2 4 1 3　1を動かす
一回動かしたものはswapに関係なくなる
"""

N = getN()
B = [0] + getList()
B = [[B[i], i] for i in B]
B.sort(reverse = True)

bit = BIT(N + 1)

ans = 0
# 今までi - 1個置いた
for i, (val, ind) in enumerate(B[:-1]):
    # 左にある自分より大きいもの vs 右にある自分より大きいもの
    ans += min(bit.get(ind), bit.cum(ind, N + 1))
    bit.add(ind, 1)

print(ans)


# ARC033 C - データ構造
# 座圧BIT
Q = getN()
que = [getList() for i in range(Q)]

# データに入れる数字を抽出する
A = []
for t, x in que:
    if t == 1:
        A.append(x)
# 座標圧縮
# alter: A[i] → alt_A[i]
# rev: alt[i] → A[i]
def compress(array):
    s = set(array)
    s = sorted(list(s))
    alter = {}
    rev = {}
    for i in range(len(s)):
        alter[s[i]] = i
        rev[i] = s[i]

    return alter, rev

alter, rev = compress(A)

limit = Q + 1
bit = BIT(limit)
for t, x in que:
    if t == 1:
        bit.add(alter[x] + 1, 1)
    else:
        # xを超えないギリギリの場所が1-indexで与えられる
        opt = bit.lowerbound(x) - 1
        # 1-indexなのでそのままprintする
        print(rev[opt])
        # xを超えないギリギリの場所の一つ右を-1する
        bit.add(opt + 1, -1)

# AGC005 B - Minimum Sum

"""
全ての連続部分列について、その最小値の総和を求めよ
N = 3
A = [2, 1, 3]の時
[2]:2 [1]:1 [3]:3
[2, 1]:1 [1, 3]:1
[2, 1, 3]:1
合計9
BITを使うと思う
小さいものから順に置いていく
iが最小値を取る領域[l, r]を求める
1を置く
[ , 1, ]
この時、左端は1番目、右端は3番目までを領域に含めることができる
左側は2 - 1 + 1 = 2通り、右側は3 - 2 + 1 = 2通りある
ans += (2 - 1 + 1) * (3 - 2 + 1) * 1
2を置く
[2, 1, ]
左端は1番目、右端も1番目
"""

N = getN()
A = getList()
index = [0] * (N + 1)
for i in range(N):
    index[A[i]] = i + 1

bit = BIT(N)
ans = 0
for i in range(1, N + 1):
    c = bit.get(index[i]) # 左側にあるフラグの数を求める
    # フラグがc個になる場所 + 1、フラグがc + 1個にある場所 - 1を求める
    # つまり、
    # 左側にある自分より小さいもののうち最も右側にあるもの + 1
    # 右側にある自分より小さいもののうち最も左側にあるもの - 1
    # の場所を求める
    l, r = bit.lowerbound(c) + 1, bit.lowerbound(c + 1) - 1
    ans += (index[i] - l + 1) * (r - index[i] + 1) * i
    bit.add(index[i], 1) # 自身を置く
print(ans)

# ARC069 E - Frequency

"""
N個の山がある
石の数が最大の山のうち最も前の番号をsにappend
石を一つとる
これを繰り返す

Sが辞書順で最小の数列になるようにした時、sに数はそれぞれいくつずつ含まれるか
A = [1, 2, 1, 3, 2, 4, 2, 5, 8, 1]の時
Sの最終的な長さはsum(A)

S = []
S = [9]: 一つ目はどういう操作をしても共通
出来るだけ前の方のをindexに指定したい
最大値の位置を出来るだけ前に寄せるためには？
現在より前の数字について最大の数字に移動する セグ木?

現在より前の数字について最大の数字まで数を減らす
それより後ろの数字についてnextの数字まで減らす
A = [1, 2, 1, 3, 2, 4, 2, 5, 5, 1]
1 + 1つの5を4まで下げる
A = [1, 2, 1, 3, 2, 4, 2, 5, 5, 1]

前からとって行った時の最小値の場所しか加算されない
この場合[1, 2,  , 3,  , 4,  , 5, 8,  ]
index = 9についてindex以降の数字を全て5まで下げる
ans[index] += index以降の5以上の部分
index = 8についてindex以降の数字を全て4まで下げる
ans[index] += index以降の4以上5以下の部分
5以上を加算、４以上４以下を加算、３以上３以下を
この場所にどのように加算するか
全てのindexについてO(1)で答えるか？
５以上のものを足す、４以上のものを足す...

各場所ind_l[i]についてそれより右側の部分のunder以上upper未満の部分について
総和を求める

BITを使って
ある範囲内のunder以上の場所の数を答える　これは簡単
          upper以下の場所の数を答える　これも簡単 bitの結果を足し引きすればOK

"""

N = getN()
A = getList()

cnt = [] # 数字iがどこにあるか
ma = [] # 1 ~ i個目までの最大値
for i in range(N):
    cnt.append([A[i], i + 1])
    if i == 0:
        ma.append(A[i])
    else:
        ma.append(max(ma[-1], A[i]))

ind_l = [] # 加算する場所
for i in range(N - 1, 0, -1):
    if ma[i - 1] < ma[i]:
        ind_l.append(i + 1)
ind_l.append(1)
ma.insert(0, 0) # 1-indexに修正した方がいい
ma.insert(0, 0)

cnt.sort()

upper = max(A)
bit = BIT(N)
ans = [0] * (N + 1)

# 自分より右側のunder ~ upperを足し合わせる
for i in range(len(ind_l)):
    index = ind_l[i]
    under = ma[ind_l[i]]
    left = 0
    while cnt and cnt[-1][0] > under:
        p, ind = cnt.pop()
        left += max(0, upper - p) # upperに到達しない部分について控除分
        bit.add(ind, 1)
    ans[index] = bit.cum(index, N + 1) * (upper - under) - left
    upper = under

for i in ans[1:]:
    print(i)

# ARC075 E - Meaningful Mean

N, K = getNM()
A = getArray(N)

# 連続部分列: imos, 尺取り法, セグ木, 数え上げdpなどが使えそう
# 算術平均がK以上であるものは何個あるでしょうか？ 尺取りっぽい
# → 平均なので尺取りではない　{100, 1 100...100}みたいな場合

# 平均なので各項をKで引いて見ようか
# N, K = 3, 6
# A = [7, 5, 7] の場合
# A = [1, -1, 1]になる 累計が0以上のもの → これだとO(n2)かかる
# 右端rを決めた時にペアになる左端lはいくつあるか

# N, K = 7, 26
# A = [10, 20, 30, 40, 30, 20, 10]の時
# imos = [0, -16, -22, -18, -4, 0, -6, -22]
# l ~ r区間の平均 = imos[r] - imos[l - 1] これが0以上なら
# = imos[r] >= imos[l - 1]なら
# imos[b] - imos[a] >= 0になるペアがいくつあるかをO(n)で

# つまり
# imos上のimos[i] = bについてより左側にb以下の数はいくつあるか

A = [i - K for i in A]
imos = [0]
for i in range(N):
    imos.append(imos[i] + A[i])
mi = min(imos)
imos = [i - mi for i in imos] # imosの全ての要素が0以上になるように調整
N += 1

# 座標圧縮BIT
# alter: A[i] → alt_A[i]
# rev: alt[i] → A[i]
def compress(array):
    s = set(array)
    s = sorted(list(s))
    alter = {}
    rev = {}
    for i in range(len(s)):
        alter[s[i]] = i
        rev[i] = s[i]
    return alter, rev

alter, rev = compress(imos)
limit = N + 1
bit = BIT(limit)
ans = 0
for i in range(N):
    # 自身以下の数字が左にいくつあるか
    ans += bit.get(alter[imos[i]] + 2) # 変換してから調べる
    bit.add(alter[imos[i]] + 1, 1) # 変換してからレコード

print(ans)
