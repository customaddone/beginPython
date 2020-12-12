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

# ABC027 C - 倍々ゲーム
# ２人が最善を尽くす時、どちらが勝つか
# パターン1:ある状態になるように収束させれば必ず勝つ
# パターン2:ある場所を目指せば必ず勝つようになる
# パターン3:最初の配置のためどんな方法を取っても必ず勝つ

# まずは全通り試してみる　その中で勝ちが偏っている部分がある
N = getN()
k = N
depth = 0
while k > 1:
    k //= 2
    depth += 1
x = 1
cnt = 1
if depth % 2:
    while x <= N:
        if cnt % 2:
            x *= 2
        else:
            x *= 2
            x += 1
        cnt += 1
    if cnt % 2:
        print("Takahashi")
    else:
        print("Aoki")
else:
    while x <= N:
        if cnt % 2:
            x *= 2
            x += 1
        else:
            x *= 2
        cnt += 1
    if cnt % 2:
        print("Takahashi")
    else:
        print("Aoki")

# ABC048 D - An Ordinary Game
# 最終的にどのような形で終わるか
S = input()
if (S[0] != S[-1]) ^ (len(S) % 2):
    print('Second')
else:
    print('First')

# ABC059 D - Alice&Brown
# まずは全通り試してみる

# 最終形をイメージする →
# 1 0 操作出来ない　終わり
# 1 1 操作出来ない　終わり
# 逆に2 0 や 3 0 なら操作できる
# 2以上開く、０か１開くを繰り返す
X, Y = getNM()
X = int(X)
Y = int(Y)

if (X - Y) ** 2 > 1:
    print("Alice")
else:
    print("Brown")

# AGC033 LRUD Game

"""
制約よりゲーム木とも違う
つまりnim
スタート地点にコマが置いてある　これを２人で動かす
S[i]の方向に動かす、もしくは動かさない
盤上から落ちるか残るか
逆から見てみると

最適行動　とは？
中央に寄るように、もしくは遠ざかるように？

全ての行動をシミュレートして偏りを探す
RとLの数の差、UとDの数の差によって勝敗がわかる

高橋くんが如何なる行為をしても青木くんは盤上に残すことができる
青木くんが如何なる行為をしても高橋くんは盤上から落とすことができる

高橋くんは駒の振れ幅を大きくする
青木くんは駒の振れ幅を小さくする
基本高橋くん有利？

2人は相手の行動を先読みできるか
あとで相手がRを大量に持っている　→　できるだけ左にずらす
最後のL or Rの処理のあと、コマが残っている
相手の最悪の行動に対応できるか
高橋と青木のLRUDの差で考える
LL
  RRRの場合

２人が最適な行動をするとは
相手が最悪の行動をしてくるということ
コマが一番左にいても絶対に落とせる
L, R, U, Dのそれぞれが独立に
R, L, D, Uと対戦できる
"""

H, W, N = getNM() # H:縦 W:横
start = getList()
S = input()
T = input()

LRUD_range = [start[1], start[1], start[0], start[0]]

for i in range(N):
    # 高橋のターン
    if S[i] == 'L': # 高橋のL対青木のR
        LRUD_range[0] -= 1
    elif S[i] == 'R':
        LRUD_range[1] += 1
    elif S[i] == 'U':
        LRUD_range[2] -= 1
    else:
        LRUD_range[3] += 1

    if LRUD_range[0] < 1 or W < LRUD_range[1] or LRUD_range[2] < 1 or H < LRUD_range[3]:
        print('NO')
        exit()

    # 青木のターン
    if T[i] == 'L': # 高橋のR対青木のL ただしleftできるのは1まで
        LRUD_range[1] = max(1, LRUD_range[1] - 1)
    elif T[i] == 'R':
        LRUD_range[0] = min(W, LRUD_range[0] + 1)
    elif T[i] == 'U':
        LRUD_range[3] = max(1, LRUD_range[3] - 1)
    else:
        LRUD_range[2] = min(H, LRUD_range[2] + 1)

print('YES')

# AGC033 C - Removing Coins
# 木の直径 + nim

"""
最適行動する
ある形に収束する

相手の手がどうであれ
全ての通りを試してみる

木の問題であり、nimの問題である

一つ頂点を選び、コインを取る
その後他のコインを吸い寄せる
ある点iを選択する
iから各コインへの距離が1小さくなる

各コインへの最短距離の最大値が1になると負け
木なのでコインが２つ隣り合うだけになったら負け
コインの木の直径が2で回ってきたら負け
コインの木はちぎれることはない

コインの木の直径を2にする

1 - 2 - 3 - 4 - 5のパスグラフを考える
1を選ぶと木の直径は1 - 2 - 3 - 4で4になる
そのあと2を選ぶと2 - 3になり直径2で勝ち
端っこを取ると木の直径が1減る
端以外を取ると木の直径が2減る

1 - 2 - 3 - 4 - 5
firが1取る 1 - 2 - 3 - 4 → secが2取る 2 - 3
firが2取る 2 - 3 - 4 → secが4取る 3 - 4

1 - 2 - 3 - 4 - 5 - 6
fir 1取る 1 - 2 - 3 - 4 - 5 firの勝ち

相手に直径5になるように回す　
firは6か7で回ってきたら勝ち　8で回ってきたら

2 + 3 * iで回ってきたら負け 2, 5, 8...
2 * (3 * i) + 1 端を選ぶ
2 * (3 * i) + 2 真ん中を選ぶ

直径を取るパスの端じゃない点か関係ない点を取ると-2される
N = 1なら自動的に勝ち
"""

N = getN()
Q = [getList() for i in range(N - 1)]

G = [[] for i in range(N)]
for i in range(N - 1):
    s, t = Q[i]
    G[s - 1].append(t - 1)
    G[t - 1].append(s - 1)

# 木の直径を求める
def bfs(s):
    dist = [-1] * N
    que = deque([s])
    dist[s] = 1

    while que:
        u = que.popleft()
        for i in G[u]:
            if dist[i] >= 0:
                continue
            dist[i] = dist[u] + 1
            que.append(i)
    d = max(dist)
    # 全部並べて一番値がでかいやつ
    return dist.index(d), d

# 0から最も遠い点uを求める
u, _ = bfs(0)
# uから最も遠い点vとその距離を求める（つまり直径）
v, d = bfs(u)

# 2 + 3 * iで回ってきたら負け
if (d - 2) % 3 == 0:
    print('Second')
else:
    print('First')

# 全国統一プログラミング王 予選　C - Different Strokes

"""
一つの数字を最大化できないか
結局青木さんの点数は高橋くんが選ばなかったもののBの総和になる
つまり高橋くんがi個目を選ぶとAi獲得するだけでなくBi特することになる
逆に青木さんがj個目を選ぶとBi獲得するだけでなくAi高橋くんを損させられる
高橋くん、青木さんはAi + Biが大きい順に取っていく
"""

N = getN()
dish = []
for i in range(N):
    a, b = getNM()
    dish.append([a, b, a + b])

dish.sort(key = lambda i:i[2])

ans = 0
while True:
    if dish: # 高橋くん
        a, b, total = dish.pop()
        ans += a
    else:
        break

    if dish: # 青木さん
        a, b, total = dish.pop()
        ans -= b
    else:
        break

print(ans)

# EDPC K - Stones

"""
nimする
K個から石を取る
Ai個（何回も選んでもいい）取る
N <= 100 小さい
(石の数) < min(A)となるようにすればいい
相手に上記の条件になるようにさせない　
2 4
2 3 なら 1になるようにする　もしくは相手が1になるようにさせない
K = 0なら
0: 先手が勝つ
1: 後手が勝つ

0 1 2 3 4 5
1 1 0 0 0
基本先行有利
自分が勝利するルートがあるか　なければ
自分が勝利するルートが一つでもあれば　の発想
"""

N, K = getNM()
A = getList()

# 0: 先手が勝つ
# 1: 後手が勝つ
dp = [1] * (K + 1)

for i in range(1, K + 1):
    for j in range(N):
        if i - A[j] >= 0 and dp[i - A[j]] == 1:
            dp[i] = 0
            break
    else:
        dp[i] = 1

if not dp[-1]:
    print('First')
else:
    print('Second')
