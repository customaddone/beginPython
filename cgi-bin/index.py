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
