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

# ABC013 D-阿弥陀
N, M, D = getNM()
A = getList()
A = [x - 1 for x in A]

# 1回阿弥陀を試してみる
amida = [i for i in range(N)]
for i in range(M):
    a1 = amida[A[i]]
    a2 = amida[A[i] + 1]
    amida[A[i]] = a2
    amida[A[i] + 1] = a1

# 逆にする
amida_alta = [0] * N
for i in range(N):
    amida_alta[amida[i]] = i

# ダブリング
logk = D.bit_length()

doubling = [[-1] * N for _ in range(logk)]

for i in range(N):
    doubling[0][i] = amida_alta[i]

for i in range(1, logk):
    for j in range(N):
        doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

ans = [i for i in range(N)]
for i in range(logk):
    for j in range(N):
        if D & (1 << i):
            ans[j] = doubling[i][ans[j]]

for i in range(N):
    print(ans[i] + 1)

# ABC167 teleporter
N, K = 6, 727202214173249351
A = [6, 5, 2, 5, 3, 2]
A = [i - 1 for i in A]

logk = K.bit_length()
doubling = [[-1] * N for _ in range(logk)]

# ダブリング
# 2 ** 0は１つ後の行き先
for i in range(N):
    doubling[0][i] = A[i]
for i in range(1, logk):
    for j in range(N):
        # doubling[i]はdoubling[i - 1]を２回行えばいい
        # doubling[i - 1][j]移動してその座標からまたdoubling[i - 1]移動
        doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

index = 0
# 各bitごとに移動を行う
for i in range(logk):
    if K & (1 << i):
        index = doubling[i][index]
print(index + 1)

S = 'RRLLLLRLRRLL'
N = len(S)
logk = (10 ** 5).bit_length()

doubling = [[-1] * N for _ in range(logk)]

# １回目の移動
for i in range(N):
    doubling[0][i] = i + 1 if S[i] == "R" else i - 1

# 2 ** k回目の移動
for i in range(1, logk):
    for j in range(N):
        doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

ans = [0] * N

# 10 ** 5回ぐらい回せば十分
for i in range(N):
    ans[doubling[logk - 1][i]] += 1

print(*ans)

# p307 ダブリング
N = 3
M = 10
que = [
[0, 3],
[3, 7],
[7, 0]
]

alta = []
for i in range(N):
    s, t =  que[i]
    if s < t:
        alta.append([s, t])
        alta.append([s + M, t + M])
    else:
        alta.append([s, t + M])
alta.sort(key = lambda i: i[1])

N = len(alta)

logk = (10 ** 6).bit_length()
doubling = [[-1] * N for _ in range(logk)]
for i in range(N):
    s, t = alta[i]
    for j in range(i + 1, N):
        opt_s, opt_t = alta[j]
        if t <= opt_s:
            doubling[0][i] = j
            break

for i in range(1, logk):
    for j in range(N):
        # 欄外に飛ぶようなら-1
        if doubling[i - 1][j] == -1:
            doubling[i][j] = -1
        else:
            doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

ans = 0
# 区間iからスタート
for i in range(N):
    s, t = alta[i]
    now = i
    cnt = 1
    # 超過しないよう大きいものから加算していく
    for j in range(logk - 1, -1, -1):
        opt_index = doubling[j][now]
        # 欄内に収まるかつ始点から距離M以内
        if opt_index >= 0 and alta[opt_index][1] <= M:
            now = opt_index
            cnt += 1 << j
    ans = max(ans, cnt)
print(ans)

# ヘンテコ辞書
# ダブリング不使用ループ
N, A = getNM()
K = getN()
B = getList()
A -= 1
B = [i - 1 for i in B]

visited = [-1] * N
visited[A] = 1

cnt = 1
to = B[A]

while cnt < K:
    cnt += 1
    if visited[to] >= 0:
        cnt += ((K - cnt) // (cnt - visited[to])) * (cnt - visited[to])
        visited = [-1] * N
    visited[to] = cnt
    to = B[to]

print(to + 1)

class Roop:
    def __init__(self, array):
        self.n = len(array)
        self.array = array
        # ループ検出
        self.roops = []
        # iはどのループのものか
        self.roop_dict = [-1] * self.n
        # ループ内の何番目にあるか
        self.opt_dic = [-1] * self.n
        ignore = [-1] * self.n
        cnt = 0
        for i in range(self.n):
            if ignore[i] >= 0:
                continue
            opt = [i]
            # opt内の何番目にあるか
            self.opt_dic[i] = 0
            c = 1
            # 探索したらフラグを立てる
            ignore[i] = cnt
            # i → array[i]
            to = array[i]
            # ループが詰まるまで回す
            while True:
                if ignore[to] == cnt:
                    # 作成してないならループ作成
                    for j in range(self.opt_dic[to], len(opt)):
                        self.roop_dict[opt[j]] = cnt
                    self.roops.append(opt[self.opt_dic[to]:])
                    # 次のループはcnt + 1番
                    cnt += 1
                    break
                opt.append(to)
                ignore[to] = cnt
                self.opt_dic[to] = c
                c += 1
                to = array[to]

    # xがどの番号のループにあるか
    def roop_n(self, x):
        return self.roop_dict[x]

    # xが入っているループは何か
    # ループ内になければFalse
    def inspect(self, x):
        if self.roop_n(x) == -1:
            return False
        return self.roops[self.roop_dict(x)]

    # ループの大きさ
    def roop_len(self, x):
        return len(self.roops[self.roop_n(x)])

    # xからk回移動してどの場所に行けるか
    def move(self, x, k):
        cnt = k
        to = x
        # ループに入る前にどのルートを通ったか
        # スタート地点から既にループに入っていた場合、headは空になる
        head = []
        # ループ脱出後どのルートを通るか
        tail = []
        # 何回ループしたか
        time = -1
        res = 0
        while cnt > 0:
            to = self.array[to]
            cnt -= 1
            # まだループしておらず、踏んだ場所がループ内にある場合
            if time == -1 and self.roop_n(to) >= 0:
                r = self.roops[self.roop_n(to)]
                time = (cnt // len(r))
                cnt -= time * len(r)
            # ループ前なら
            if time == -1:
                head.append(to)
            # ループ後なら
            else:
                tail.append(to)
        # 例: N, K = 6 727202214173249351
        # A = [6, 5, 2, 5, 3, 2]の時
        # 1回目の移動 1 → 6
        # 2回目の移動 6 → ### ここからループが始まる ### → 2
        # ... 242400738057749783回ループ
        # 727202214173249351回目の移動 3 → 2
        # to, head, tail, time = (1, [5], [1], 242400738057749783)
        return to

N, A = getNM()
A -= 1
K = getN()
B = [i - 1 for i in getList()]
roop = Roop(B)
print(roop.move(A, K) + 1)

"""
# ABC167 D - Teleporter
N, K = getNM()
N -= 1
A = [i - 1 for i in getList()]
roop = Roop(A)
print(roop.move(0, K) + 1)
"""

"""
# ABC175 D - Moving Piece
N, K = getNM()
P = [i - 1 for i in getList()]
C = getList()
# ループ検出
roop = Roop(P)
# 各ループごと調べる
ans = -float('inf')
for r in roop.roops:
    n = len(r)
    # ループに対応するスコアリストを用意
    alta = []
    for i in range(n):
        alta.append(C[r[i]])
    # １回ループすると何点getできるか
    one_roop = sum(alta)
    alta += alta
    imos = [0]
    for i in range(len(alta)):
        imos.append(imos[i] + alta[i])
    t = min(n, K)
    for i in range(n):
        # 長さ1からtまでの区間の総和の最大値を探索
        for j in range(1, t + 1):
            if one_roop >= 0:
                opt = (imos[i + j] - imos[i]) + ((K - j) // n) * one_roop
            else:
                opt = imos[i + j] - imos[i]
            ans = max(ans, opt)
print(ans)
"""
