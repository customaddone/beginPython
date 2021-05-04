from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement


import sys
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

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(1000000)
INF = float('inf')
eps = 10 ** (-10)
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

# 普通にゲーム木を考える
# N = 10の場合
# 自分のとこに11で回ってきたら勝利する(相手がNを超えてしまったため)
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
# 10で回ってきたら次20か21になり自分は敗北する 6 ~ 9も同様
# [-1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 1]
# つまりiについてi * 2, i * 2 + 1どちらの遷移も1の場合自分は敗北する
# 連続する0のボーダーは一つ前の1のボーダーをkと置くと(k + 1) // 2

# 敗北するマスを埋める場合は遷移先全てが前のボーダーにかかるように
# 勝利するマスを埋める場合は遷移先が前のボーダーにギリギリかするように

N = getN()
N += 1
rev = 1 # 1(ここに到達すると勝ち)のボーダー
while N > 1:
    if rev > 0: # 次0のボーダーを決める
        N = (N + 1) // 2
    else:
        N = N // 2
    rev *= -1

if rev > 0:
    print('Takahashi')
else:
    print('Aoki')

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

# ARC112 C - DFS Game

"""
最終的にコインは全てなくなる
移動する場合はコインの回収ができないのでやらない方がいい？
高橋くんと青木くんは同じ戦略

部分木の偶奇によって変わりそう
相手がコインをとった場合は自分は移動するしかない

コインの乗った箇所に乗られるとそこから葉まで全てかっさらわれる
そこから戻る
当然そこから根までは何もない
奇数個戻るとターンが入れ替わる

その途中で枝があればまたそこからスタートする
どの枝を選ぶかは任意
任意で選ぶ場所に戦略性

一回葉まで行ったら下の部分木から処理される
戦略通りいけば部分木についてどのようだったかが一意に定まりそう
小さい部分木で考える

部分木の根に移動した状態でターンがスタートすれば
部分木のコインを全て刈った状態でターンが回ってくるのはだれ？
逆転するかそのまんまか　コインの枚数は

子がない場合は

親要素から子に移動した
手番は逆転している方がいい
必ず手番が入れ替わるものを選ぶ

手番が入れ替わるものは小さい順に回収される

dfsを行う
保持する情報は
fore/rev 親頂点から本頂点に移動した場合、親頂点に戻った場合に手順が入れ代わってるかどうか
val: 親頂点から本頂点に移動した場合、自分はいくら獲得できるか

子頂点の情報を元にresを作成する
f/r: ()子頂点のrの数 + 1) % 2 == 0ならf 1ならr
val: (+でforeのもの) + (rの大きい方から奇数個目) - (rの大きい方から偶数個目) + (-でforeのもの) * (-1 ** (len(r) == 0))
(-でforeのもの)はrの長さが偶数であればこちらが引き受ける
"""

N = getN()
P = getList()
E = [[] for i in range(N)]
for i in range(N - 1):
    E[P[i] - 1].append(i + 1)

# turn: 0なら順番そのまま 1なら逆転
def dfs(u):
    turn = 0
    # point計算用　移動した先のコインは必ず取られるのでまず-1
    point = -1
    rev = []
    fore_minus = 0
    for v in E[u]:
        t, val = dfs(v)
        turn += t
        # 順向きなら
        if t == 0:
            # +の値なら
            if val >= 0:
                point += val
            else:
                fore_minus += val
        # 逆向きになるなら
        else:
            rev.append(val)
    # 計算
    rev.sort(reverse = True)
    # revを大きい方から交互にとっていく
    rev = [rev[i] if i % 2 == 0 else -rev[i] for i in range(len(rev))]
    point += sum(rev)
    # -でforeのものはその時の手番の人が全てとる
    if len(rev) % 2 == 0:
        point += fore_minus
    else:
        point -= fore_minus

    return (turn + 1) % 2, point

# 頂点0に移動する人、つまり青木くんのプラマイが出てくる
t, p = dfs(0)

print((N - p) // 2)
