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

# Mujin Programming Challenge 2017 A - Robot Racing

"""
N体のロボット
座標は全て異なり1 <= xi <= 10 ** 9 二分探索できる
dpしたいけどxが大きいのでdpできない
現在の座標から-1, -2のどちらかに進める　ダブルと他のを待たないといけない
N体のロボットがゴールする順番は何通りありますか
トポソか？
トポソの通りは求められる
どれがどれより先でないといけないかわかれば

前からdpしていくのかな
理想的な状態であればN!

ロボットiがjより先にゴールする条件
1 2 3 の場合
全部で3!
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1 ある
ただし3は1, 2より先にゴールできない
  , i, , jの場合
  , i, j,
 j, i,  ,でjはiより先に行ける

  , i, j,  の状態にできればjはiを飛び越せる
  , i, j, lの場合でも
 i,  , j, lとすればiの直後に隙間ができるので飛び越せる
できない条件は
a, b, c, i, j, lだとしても適当にa, bを動かしたら
 ,  ,  , i, j, l前に隙間ができるので動かせる
iが2番目以降にあれば後ろの駒は飛び越せそうだけど
jがiを飛び越せる→同じルートを通ってその後ろのkも飛び越せる

連なってる部分があると難しくなるみたい
トポソではなさそう

8
1 2 3 5 7 11 13 17 だと10080(8! // 4)

iが一番最初にゴールできるか
１番目にあるとできない では2番目は
1, 2, 3, , 5, 6, 7　なら
 , 2, 3, , 5, 6, 7
lim = 現在の場所 // 2個以下の駒があれば通過できる　偶数番目だとお得
前に駒がplace[i] // 2個しかなければ1位通過できる
つまり (i - (place[i] // 2)) + 1位通過できる
1, 2, 3の場合
2 1位通過はできる
3 2位通過はできる
前にある駒 - lim位通過はできる
1, 2, 3, 4位の場合
 , 2, 3, 4 4は2位通過はできる
1, 2, 3, 4, 5の場合
 , 2, 3, 4, 5 5は3位通過はできる
1: (0 - (1 // 2)) + 1 = 1
2: (1 - (2 // 2)) + 1 = 1
3: (2 - (3 // 2)) + 1 = 2
4: (3 - (4 // 2)) + 1 = 2
5: (4 - (5 // 2)) + 1 = 3

更にi番目がn番目以降でしかゴールできないなら、それより後ろのjがn - 1番目でゴールできるわけない
l[i] = max(l[i - 1], opt)
1, 2, 3, 4, 5
3が一つ遅延するので4, 5も遅延する
4に影響するのは2 2は遅延しないが4自身が遅延するのでdp[2] + 1
5は3が遅延するし5自身も遅延する
前の駒は全て1, 3, 5...と配置する
配置できない場合は+= 1
"""

N = getN()
X = getList()
l = [1] * N
now = 0
cnt = 1

for i in range(N):
    l[i] = cnt
    if X[i] < 2 * now + 1:
        cnt += 1
    else:
        now += 1

power = [0] * (N + 1)
for i in range(N):
    power[l[i]] += 1

# 最高位が決まっているときの順列の通りの求め方
ans = 1
acc = 0
for i in range(N):
    acc += power[i + 1]
    ans *= acc
    ans %= MOD
    acc -= 1

print(ans % MOD)

# AGC43 B - 123 Triangle

"""
1 2 3 1
 1 1 2
  0 1
   1

2 3 1 1 3 1 2 3 1 2
 1 2 1 2 2 1 1 2 1
  1 1 1 0 1 0 1 1
   0 0 1 1 1 1 0
    0 1 0 0 0 1
     1 1 0 0 1

途中から0と1にしかならない
0と2のみであればその後も0と2のみになる
1 2 0 2 0 2 2 0
 1 2 2 2 2 0 2
  1 0 0 0 2 2
   1 0 0 2 0

少しでも1が混ざれば答えは0か1か
x_left xor x_right が xの答えになる
一行の並びだけで一つ上を予想できるか
0と2は同じものとして扱う

0 0 1 0 1 0 0 0 1 0 1 0 0
 0 1 1   1 0 0   1 1 1 0
  1 0     1 0     0 0 1
   1       1       0 1
                    1

1 0 1 0 1 1 0 0
 1 1 1   0 1 0
  0 0     1 1
   0       0

1 0
 1  右に1を置くと 1 0 0を置くと 1

1 1 1 1 1 0 1 1
 0 0 0   1 1 0
  0 0     0 1
   0       1

頂点からアクセスするルート（寄与する回数）を考えると
パスカルの三角形みたいになる
1 4 6 4 1 頂点から左から2つめにアクセスする回数は4回
 1 3 3 1
  1 2 1
   1 1
    1

# nCrの偶奇判定　Lucasの定理
"""

N = getN()
A = list(input())
A = [int(i) - 1 for i in A]
B = [0 if i % 2 == 0 else i for i in A]

cnt = 0
for i in range(N):
    if B[i] % 2: # 1である
        # nCrの偶奇判定　Lucasの定理
        if (N - 1) & i == i:
            cnt += 1

if cnt % 2:
    print(1)
else:
    if 1 in B:
        print(0)
    else:
        c = [i // 2 if i % 2 == 0 else i for i in A]
        cnt = 0
        for i in range(N):
            if c[i] % 2:
                if (N - 1) & i == i:
                    cnt += 1
        if cnt % 2:
            print(2)
        else:
            print(0)

# ABC078 C-HSI

"""
NケースのうちMケースでTLEする
Mケースだけ1/2の確率で正解する
一回で通る確率1/2 ** M
一回で通らない確率1 - (1/2 ** M)
これが続く
1/2 ** M = tと置くと
一回で通る確率　t
二回で通る確率　(1 - t) * t
三回で通る確率　(1 - t) ** 2 * t... これの総和
n回で通る分の期待値 n * (1 - t) ** (n - 1) * t
n+1回で通る分の期待値 (n + 1) * (1 - t) ** n * t
回答に失敗した場合、またイーブンからスタートする
求める期待値をyとすると、y = x + (1 - p)y
"""

N, M = getNM()
total = 1900 * M + 100 * (N - M)
print(total * (2 ** M))

# ABC189 F - Sugoroku2

"""
期待値計算　期待値dp
まずは穴がない状態を考える

確率はすぐに求まる
imosすればO(N)で
期待値？
P[i] * E[i]をMで割ったものを足していけばいいのか
なんか数が小さくなる　なんかをかける
iを絶対訪れるとは限らない！
訪れる確率の逆数をかける

問題は簡略化できる
双六はSとGのみ
確率P_gでゴールでき、値がE_gプラスされる
確率(1 - P_g)で振り出しに戻り、値がE_hプラスされる
ゴールするのにかかるルーレットの回数の期待値はP_g
dp[i]: i回でゴールする時の期待値とすると
1回目でゴールする場合 確率はP_g, 期待値はE_g
2回目でゴール (1 - P_g)P_g, E_g + E_h
3回目でゴール (1 - P_g)^2P_g, E_g + E_h * 2...
"""
N, M, K = getNM()
A = getList()
A = set(A)

# 1-indexにする
# 0: スタート 1 ~ N - 1:一般マス N ~ N + M - 1:ゴールマス
P = [0] * (N + M + 1)
P[0] = 1
rec = [0] * (N + M + 1)

# 0からマスiに到達する確率を求める
for i in range(N + M + 1):
    if 0 < i:
        rec[i] += rec[i - 1]
    P[i] += rec[i]
    P[i] = max(0, P[i])

    if i < N and not i in A:
        rec[i + 1] += P[i] / M
        rec[i + M + 1] -= P[i] / M

# 0からマスiに到達する期待値を求める
E = [0] * (N + M + 1)
rec = [0] * (N + M + 1)

for i in range(N + M + 1):
    if 0 < i:
        rec[i] += rec[i - 1]
    E[i] += rec[i]
    E[i] = max(0, E[i])
    if P[i]:
        E[i] = E[i] / P[i]

    if i < N and not i in A:
        rec[i + 1] += P[i] * (E[i] + 1) / M
        rec[i + M + 1] -= P[i] * (E[i] + 1) / M

# 一巡でゴールする確率と期待値、振り出しに戻る確率と期待値を計算する
P_g, E_g = 0, 0
P_h, E_h = 0, 0
for i in range(1, N + M):
    if i in A:
        P_h += P[i]
        E_h += P[i] * E[i]
    if N <= i:
        P_g += P[i]
        E_g += P[i] * E[i]

if P_g < 10 ** -12:
    print(-1)
else:
    # 最後のスタートを引き当てるのにかかる回数の期待値はE_h / (1 - P_h)
    # ゴールに行くのにかかる回数の期待値はE_g / P_g
    print(E_h / (1 - P_h) + E_g / P_g)
