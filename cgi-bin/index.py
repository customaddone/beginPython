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

# NOMURA プログラミングコンテスト 2020 C - Folia
"""
N = 3
A = [0, 1, 1, 2]の場合
葉の数を求める
まず完全二分木から考える
ここから取り除く
深さ3の葉は4つある
深さ4の葉は8つある
深さnの葉は2 ** (n - 1)つある
深さ3の葉は4つある完全二分木について
A = [0, 0, 0, 4]
深さ3の葉を一つ刈ると
A = [0, 0, 0, 3]
二つ刈ってみる　この時、１つ目と同じ親のを刈ると
A = [0, 0, 1, 2]
違うのを刈ると
A = [0, 0, 0, 2]
根となる頂点を１つ作る
A[0] = 1ならその頂点は葉（下に頂点を繋げない)
A[0] = 0ならその頂点は生きる
頂点の最大値を求めるなら
なるべく大きく分岐させた方がいい
エッジ貼らなくても頂点数求めるだけでいい
A[i]を探索するたびに ans += する
現在用意している仮の頂点数を保持しておく
確定させた頂点数も抑えておく
A = [0, 0, 1, 0, 2]を逆から見ると
psuedo = [1, 2, 4, 8, 16]
psuedoのそれぞれとA[4]どちらか小さい方をpsuedoから引く
psuedo = [0, 0, 2, 6, 14]
left[0] ~ left[i]のそれぞれでA[i]を引けるだけ引く
順に見ると
psuedo = []
left = [] # ansに加える値
A[0] = 0
psuedo = [1]
left = [1]
A[1] = 0
psuedo = [1, 2]
left = [1, 2]
A[2] = 1
psuedo = [1, 2, 3]
left = [0, 1, 3]
A[3] = 0
psuedo = [1, 2, 3, 6]
left = [0, 1, 3, 6]
A[4] = 2
psuedo = [1, 2, 3, 6, 10]
left = [0, 0, 1, 4, 10]
葉にならない点の上限を考える
"""

# 根から探索するか
# 葉から探索するか

# 私は根から
# 総和には累積和が効く
N = getN()
A = getList()

# 深さ0の二分木の場合
if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()

if A[0] == 0:
    psuedo = [1]
    left = [1] # 確定させる用
else:
    psuedo = [0]
    left = [0]

alta = deepcopy(A)
for i in range(N - 1, -1, -1):
    alta[i] += alta[i + 1]
ma = max(alta)

# i + 1番目について調べる
for i in range(1, N + 1):
    opt = min(psuedo[-1] * 2, ma) # stop指数爆発 今回max(alta)以上の数字は必要ない
    psuedo.append(opt)
    left.append(opt)
    if psuedo[-1] - A[i] < 0:
        print(-1)
        exit()
    psuedo[-1] -= A[i]
    # 確定させていく
    """
    明らか追いつかないので累積する
    for j in range(i, -1, -1):
        if dete[j] == 0:
            break
        add = min(dete[j], A[i])
        ans += add
        dete[j] -= add
    """

ans = 0

for i in range(N + 1):
    ans += min(left[i], alta[i])
print(ans)

# ARC030 B - ツリーグラフ
# 全ての宝からrootに登っていく
# 通ったところをignoreにし、再度踏むことがないように
# rootから探索していき、宝石があればその親と親の親と...の頂点を全てTrueにする
# vに宝石がなくても、子孫にあればTrueにする

def dfs(par, v): # dfsは親持っておいたほうがいい
    res = 0
    for i in dist[v]:
        if i == par:
            continue
        opt = dfs(v, i)
        if opt > 0: # 宝石があるルートの帰り道
            res += opt + 2 # これまでの累計 + iの分
        elif H[i]: # ここまで宝石が見つかってなかったが、新たに宝石がある
            res += 2

    return res

N, X = getNM()
X -= 1
H = getList() # フラグが立っている部分だけ
dist =[[] for _ in range(N)]
for i in range(N - 1):
    a, b = getNM()
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

print(dfs(-1, X))

# AGC014 B - Unplanned Queries

"""
どこかの点を基準とする
・どの辺を見ても書かれている数が偶数になった
性質を満たす木が存在するか
色々な木で考えてみよう
最終的に最適な木の構造がわかる？
頂点xを基準に見ると
x - 1 - 2の木の場合 [1, 2]のクエリは
x - 1 ① 2 xを経由すると
x ② 1 ① 2
他の辺の偶奇を変えずに1 - 2間だけ数字を加算することができた
最も単純なスターグラフを考えると、x - i間の辺の数字 = クエリに何回iが出たか
適当な頂点を根として、根付き木にする。この根を r とする。
・クエリ(p, a) + (p, b)とクエリ(a, b)は同じ
まず、クエリ (a, b) を考えたとき、これ を (r, a), (r, b) と分解することができる。
これは、(a, b) の LCA を p としたとき、クエリ (a, b) ではパス a − p, b − p に +1 しており、
クエリ (r, a), (r, b) ではパス a − p, b − p に +1、パス r − p に +2 するため、
mod 2 で考えると同一視できるので明らかである。
基準点をrとすると、クエリ全体では (r, i (i = 1 ~ N))を繰り返すことと同値である
(r, v(vはrから一番深い点))のクエリを偶数回行う時、途中の辺についても偶数回加算されている
"""

N, M = getNM()
list = [0] * (N + 1)
for i in range(M):
    a, b = getNM()
    list[a] += 1
    list[b] += 1

for i in range(1, N + 1):
    if list[i] % 2 != 0:
        print('NO')
        exit()
print('YES')

# AGC013 B - Hamiltonish Path

"""
木構造ではない
N頂点にM辺
・２個以上の頂点を通る
・同じ頂点を通らない
・パスの少なくとも一方の端点と直接辺で結ばれている頂点は、必ずパスに含まれる
いくつかあるうちの一つ答えよ
端点と端点をつなぐと輪になる
端点の頂点数は2でないといけないのでは　そんなことはない
端点の候補はどんなものがあるか
端点の１つ目はなんでもいいのか
グリッドグラフを考えた場合に中央の点を指定してもうまく条件を満たすのでいけそう
ただし、子要素に葉があればだめ
端点に葉が2つあれば余裕
端点を一つ選ぶ　→
隣接する辺を全て通るパスを考える　
7 8
1 2
2 3
3 4
4 5
5 6
6 7
3 5
2 6　の時
もし2 6のパスがなければ3を端点にできない
パスグラフを考えると
パスグラフの端っこ２つを端点にしないと作れない
大元となるパスグラフを見つける
寄り道しないといけない場合であってもすぐ戻ってこれるような
端点を一つ決める
端点を2にしてもう片方の端点を考える時、1が邪魔
端点を2から1にずらせれば楽
適当な点１つを選んでそこから端点1に行くパス、端点2に行くパスを書いていく
これ完全グラフだとTLEするんじゃ？
今回Mの数が小さい
作れる最大の完全グラフはN = 400 (N(N + 1) // 2 = 80000ぐらい)なのでOK
"""

N, M = getNM()
dist = [[] for i in range(N)]
for i in range(M):
    a, b = getNM()
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

parent = [-1] * N
ignore = [0] * N
ignore[0] = 1
dot1 = 0
dot1_flag = True
dot2 = 0
dot2_flag = True

# 端点が見つかる（行き止まりになる）まで探索
while dot1_flag or dot2_flag:
    dot1_flag = False
    for i in dist[dot1]:
        if ignore[i] == 0:
            ignore[i] = 1
            parent[dot1] = i
            dot1 = i
            dot1_flag = True
            break

    dot2_flag = False
    for i in dist[dot2]:
        if ignore[i] == 0:
            ignore[i] = 1
            parent[i] = dot2
            dot2 = i
            dot2_flag = True
            break

ans = [dot2 + 1]
now = dot2
while now != dot1:
    now = parent[now]
    ans.append(now + 1)

ans = list(reversed(ans))

print(len(ans))
print(*ans)

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


# AGC039 B - Graph Partition

"""
N頂点M辺
N <= 200
O(n ** 3)までいける
ワーシャルフロイドか
01
10
1 - 2

頂点集合V1, V2, V3...をできる限り作る
頂点集合の最大値
どの辺も番号が隣り合う頂点集合の頂点同士をつなぐ
頂点を分解する
いろいろやってみる

頂点を一つずつ前から調べてみる
頂点1をV1に入れると
V1とVkだけ不利な気がする

隣接する頂点は隣に置く
距離が2ある頂点については自身と同じ場所に置ける
[[1, 3, 4], [0, 2, 5], [1, 3], [0, 2], [0], [1]]の場合

0を置く 0
1を置く 0 1
2を置く 0 1 2
3を置く時 0 - 3にエッジがあるため2の向こうに置くことはできない
0 1 2
  3

全ての辺について条件を満たす
辺をいい感じに配置する
1, 3について、[0, 2]は共通して隣にいないといけない
輪ができる　輪を潰す

最短距離の位置に配置すれば良い
繋がってなければ何してもいい

偶数か奇数か　繋がっていれば隣
２つに分けることは可能か
距離奇数のものを向こうに、偶数のものをこっちに
判定可能
距離を伸ばすということは？

まず２つのグループに分けられるか
分けられるならAi ~ Ajの最短距離の最長が答え
"""

N = getN()
S = [[int(i) for i in list(input())] for j in range(N)]

edges = [[] for i in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j] == 1:
            edges[i].append(j)

# まず２つのグループに分けられるか
group = [-1] * N
group[0] = 0

pos = deque([0])
while pos:
    u = pos.popleft()
    for i in edges[u]:
        if group[i] == -1: # 未確定
            group[i] = 1 if group[u] == 0 else 0
            pos.append(i)
        else: # 確定済み
            if group[u] == group[i]:
                print(-1)
                exit()

# ２つのグループに分けられるなら
# Sをdistに使う
for i in range(N):
    for j in range(N):
        if i != j and S[i][j] == 0:
            S[i][j] = float('inf')

def warshall_floyd(dist):
    for k in range(N):
        # i:start j:goal k:中間地点でループ回す
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

S = warshall_floyd(S)
ans = 2 # 連結ってことは絶対に2以上
for i in S:
    ans = max(ans, max(i) + 1)

print(ans)
