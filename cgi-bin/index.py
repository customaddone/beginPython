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
# sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# codeforces 431 D. Rooter's Song

"""
antsみたいだが　それぞれどこに止まるか
スタートは同じでもまつ時間が違う
N^2解法ならわかる　ぶつかる度に取り替え

0秒時点の場所を抑える　45度下、上にあればぶつかる
つまりx + yが同じであればぶつかる
同じものならyが小さい順に入れ替わる
x + yが同じもの同士でグループを作る　順番に場所を決める
2
1
v1 と入れ替わり、3が抜ける（元々のv1の位置になる）
以下
1
v1
v2 2が抜ける　の繰り返し
# horの一番上のやつから決めていく
# horの後ろからvの小さい順にはめていく 余る
old: h3, h2, h1, v1, v2, v3, v4
new: v1, v2, v3, v4, h3, h2, h1

old: h3, h2, h1, v1, v2
new: v1, v2, h3, h2, h1
horの逆向き + verの順むき
verの順むき + horの逆向き

平面走査　45度斜めはx + y
"""

N, W, H = getNM()
Ver, Hor = defaultdict(list), defaultdict(list)
goal = {}
ans = [(0, 0)] * N

for i in range(N):
    g, p, t = getNM()
    # vertical
    if g == 1:
        Ver[p - t].append([p, i])
        goal[i] = (p, H)
    else:
        Hor[p - t].append([p, i])
        goal[i] = (W, p)

K = set(Ver.keys()) | set(Hor.keys())
for k in K:
    v, h = sorted(Ver[k]), sorted(Hor[k])
    old = h[::-1] + v
    new = v + h[::-1]
    for i in range(len(old)):
        ans[old[i][1]] = goal[new[i][1]]

for a in ans:
    print(*a)

# M-SOLUTION F-Air Safety

"""
衝突する？ Nは大きい O(N)で
飛行機2機の場合を考えると
同じ座標に来るとは？
同じ方向ならぶつからない
反対方向でもぶつからない
お互いの位置によりぶつからない方向が決まる
二点でできる四角形が正方形ならさらに方向が悪ければぶつかる
plane1がU方向の時、上方にありLかRならぶつかる
平面走査しよう
上方向と下方向に平面走査

U, Dの組み合わせはあとで処理する
現在保持しているUの飛行機についてそれぞれ判定
マンハッタン距離を考える
"""

N = getN()
P = [list(input().split()) for i in range(N)]
P.sort(key = lambda i:i[1])
for i in range(N):
    P[i][0] = int(P[i][0])
    P[i][1] = int(P[i][1])

ans = float('inf')
# 下から走査する
u_d = sorted([i for i in P if i[2] == 'D' or i[2] == 'U'], key = lambda i:i[1])
up_place = {}
for x, y, dir in u_d:
    if dir == 'U':
        # yの位置は更新していく
        up_place[x] = y
    if dir == 'D':
        if x in up_place:
            ans = min(ans, (y - up_place[x]) * 5)

# 左から走査する
u_r = sorted([i for i in P if i[2] == 'R' or i[2] == 'L'])
right_place = {}
for x, y, dir in u_r:
    if dir == 'R':
        right_place[y] = x
    if dir == 'L':
        if y in right_place:
            ans = min(ans, (x - right_place[y]) * 5)

up = sorted([i for i in P if i[2] != 'D'], key = lambda i:i[1])
down = sorted([i for i in P if i[2] != 'U'], reverse = True, key = lambda i:i[1])

# 上向きに走査
posi = {} # 傾きが正のマンハッタン距離x-y left方向の飛行機がいればout
nega = {} # 傾きが負のマンハッタン距離x+y right方向の飛行機がいればout
for x, y, dir in up:
    if dir == 'U':
        # 更新していく
        posi[x - y] = y
        nega[x + y] = y
    if dir == 'L':
        if x - y in posi:
            ans = min(ans, (y - posi[x - y]) * 10)
    if dir == 'R':
        if x + y in nega:
            ans = min(ans, (y - nega[x + y]) * 10)

# 下向き走査
posi = {} # 傾きが正のマンハッタン距離x-y right方向の飛行機がいればout
nega = {} # 傾きが負のマンハッタン距離x+y left方向の飛行機がいればout
for x, y, dir in down:
    if dir == 'D':
        posi[x - y] = y
        nega[x + y] = y
    if dir == 'L':
        if x + y in nega:
            ans = min(ans, (nega[x + y] - y) * 10)
    if dir == 'R':
        if x - y in posi:
            ans = min(ans, (posi[x - y] - y) * 10)

if ans == float('inf'):
    print('SAFE')
else:
    print(ans)
