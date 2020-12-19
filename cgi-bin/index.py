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

# 包除原理
N = 100
M = 3
A = [2, 3, 8]
A.sort(reverse = True)
minus = [0] * (N + 1)

ans = 0
# (A & B & C)の個数について調べる
# → A & Bの個数を計算したものから (A & B & C)の個数を引く
for bit in range((1 << M) - 1, 0, -1):
    prim = 1
    for j in range(M):
        if bit & (1 << j):
            prim = prim // math.gcd(prim, A[j]) * A[j] # lcmの計算
    mi = N // prim
    for i in range(prim, N, prim):
        mi -= minus[i]
    if minus[prim] == 0:
        minus[prim] = mi
    ans += mi
print(ans)

# ABC162 E - Sum of gcd of Tuples (Hard)
N,K = getNM()
ans = 0
rec = [0] * (K + 1)

"""
集合A, B, Cについて
A ⊆ B　かつ B ⊆ Cとすると
集合が小さい順から数えて行って
Bを数える時にB -= A
Cを数える時にC -= Aすればダブらない
"""

for X in range(K, 0, -1):
    rec[X] = pow(K // X, N, mod)
    for i in range(2, K // X + 1):
        rec[X] -= rec[i * X] % mod
    ans += (X * rec[X]) % mod
print(ans % mod)

# ABC152 F - Tree and Constraints

"""
Nが非常に小さい
木の問題
Mの制約的にbitでもいける
小さい例から考えてみよう
M個の制約を全て満たすもの
3
1 2
2 3
1
1 3

bit dpか
u ~ vのパスを真っ白にするにはどこが白ならいいか
5
1 2
3 2
3 4
5 3
3
1 3
2 4
2 5 の時

1 ~ 3: [0, 1, 2]
2 ~ 4: [1, 2, 3]
2 ~ 5: [1, 2, 4]
1 ~ 3のパスが条件を満たす = 0, 1, 2のどれかが黒
0, 1, 2が白なら1 ~ 3は条件を満たさない

これをbitする bit dpだろ
M個のうちどれか一つでも違反するものがあれば
1 ~ 3に違反: 4, 5free 00011, [00010], [00001], [00000]
2 ~ 4に違反: 1, 5free 10001, [10000], 00001, [00000]
2 ~ 5に違反: 1, 4free 10010, 10000, 00010, 00000
2 ~ 4かつ2 ~ 5 10000, 00000
ダブったのは捨てる

集合{A1, A2...}で作る部分集合は過去の要素による部分集合とダブってないか
奇数段の集合でできてるところは引く
偶数段の集合でできてるところは足す
"""

N = getN()
dist = [[] for i in range(N)]
dist_id = {}
cnt = 0
for i in range(N - 1):
    a, b = getNM()
    dist_id[(min(a - 1, b - 1), max(a - 1, b - 1))] = cnt
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)
    cnt += 1

M = getN()
Q = [getList() for i in range(M)]

def router(n, sta, end):
    pos = deque([sta])
    ignore = [0] * n
    path = [0] * n
    path[sta] = -1

    while pos[0] != end:
        u = pos.popleft()
        ignore[u] = 1

        for i in dist[u]:
            if ignore[i] != 1:
                path[i] = u
                pos.append(i)

    route = deque([end])
    while True:
        next = path[route[0]]
        route.appendleft(next)
        if route[0] == sta:
            break

    path = []
    for i in range(len(route) - 1):
        a = route[i]
        b = route[i + 1]
        if b < a:
            a, b = b, a
        path.append(dist_id[(a, b)])
    return path

opt = []
origin = set()
for i in range(cnt):
    origin.add(i)

for u, v in Q:
    opt.append(origin ^ set(sorted(router(N, u - 1, v - 1))))

# ABC162 E - Sum of gcd of Tuples (Hard)と違うところ
# 集合Aがどの集合内に含まれるかすぐにわからないこと((2 ** M) ** 2かかる)

# パスの本数はN - 1本
S = [[] for i in range(M)]
ans = 0
for o in opt:
    res = 2 ** len(o) # 初期値
    # ダブった分を消していく
    for i in range(M - 1, -1, -1):
        for j in S[i]:
            # 奇数回重なるところについては引く
            if i % 2 == 0: # 引く
                res -= 2 ** len(j & o)
            # 偶数回重なるところは足す
            else: # 足す
                res += 2 ** len(j & o)
            S[i + 1].append(j & o)

    S[0].append(o)
    ans += res

print(2 ** (N - 1) - ans)

# ABC172E NEQ

"""
モンモール数？
個数を求めなさい
N = Mの場合
A:(M = Nの順列), B:(M = Nの順列)
N! * N!
すべて満たすもの = 全ての通り - 1個以上満たさないもの
どこか一箇所以上でAi = Biになる
どこか二箇所以上でAi = Biになる...

N箇所全てでAi = Biになる: N!通り　A固定で考えると1通り
N-1箇所以上でAi = Biになる: nCn-1箇所選ぶ　そこは同じ
あとは自由: 1!通り
N-2箇所以上: nCn-2箇所選ぶ　そこは同じ
あとは自由: 2!通り

一箇所以上: nC1 * (n-1)!通り: 1回ダブる
二箇所以上: nC2 * (n-2)!通り: 2回ダブる

N-1箇所以上: 1!通り: N-1回ダブる
N箇所以上: 0!通り: N回ダブる
L = [0] * 5
for i in permutations([i for i in range(4)]):
    cnt = 0
    for j in range(4):
        if i[j] == j:
            cnt += 1
    L[cnt] += 1
print(L)

[9, 8, 6, 0, 1]
[44, 45, 20, 10, 0, 1]

s個のAi,Biが一致しているA, Bの組みの個数は
mPs(一致しているもの) * m-sPn-s ** 2(A, Bについてあとは自由)
これがnCs個ある
Ai = Biとなっているiの個数はs個以上

ans = 0個以上一致しているもの　0個だけでいいんだけど
ans -= 1個以上一致しているもの
少なくともA1, A2が一致している集合は少なくともA1が一致している集合に含まれ、
少なくともA2, A3が一致している集合は少なくともA2が一致している集合に含まれるが、
少なくともA1, A2が一致している集合は少なくともA3が一致している集合には含まれない
小グループがnCs個あり、さらにその中で分かれていると考えれば
"""

N, M = getNM()
ans = 0
for i in range(N + 1):
    ans += (-1) ** (i % 2 == 1) * cmb(N, i) * factorial(M, i) * (factorial(M - i, N - i) ** 2)
print(ans % mod)
