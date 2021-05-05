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

# ABC025 C - 双子と○×ゲーム

"""
ここにマスを置くと...?
もっともreturnが高いものを選択する
c % 2 == 0なら直大番、c % 2 == 1なら青木番

ゲーム木の問題は両プレイヤーが
「ここに置くと最大returnが得られる選択肢」
を貪欲に選択する
ここに置くとどれだけリターンが得られるかはdfsにより探索する
"""

B = [getList() for i in range(2)]
C = [getList() for i in range(3)]

ans = sum([sum(b) for b in B]) + sum([sum(c) for c in C])
# 判定用func
def cnt(t):
    res = 0
    # b
    for i in range(2):
        for j in range(3):
            if t[i][j] == t[i + 1][j]:
                res += B[i][j]
            else:
                res -= B[i][j]
    # c
    for i in range(3):
        for j in range(2):
            if t[i][j] == t[i][j + 1]:
                res += C[i][j]
            else:
                res -= C[i][j]

    return res

T = [[-1] * 3 for i in range(3)]
def dfs(c):
    if c == 9:
        return cnt(T)

    # 直大番はもっとも値が大きい箇所、青木番はもっとも値が小さい箇所を選ぶ
    res = float('inf') * ((-1) ** (c % 2 == 0))

    # 全探索する
    for i in range(3):
        for j in range(3):
            if T[i][j] == -1:
                T[i][j] = (c % 2 == 0) # 行きがけ
                if c % 2 == 0: # 直大turnなら
                    res = max(res, dfs(c + 1))
                else: # 青木turnなら
                    res = min(res, dfs(c + 1))
                T[i][j] = -1 # 帰りがけ

    return res

# 合計ポイントがansあり、プレイヤー1 - プレイヤー2 = diffの時
# プレイヤー１: (ans + diff) // 2
# プレイヤー２: (ans - diff) // 2
diff = dfs(0)
print((ans + diff) // 2)
print((ans - diff) // 2)

# Indeedなう（予選A）D - パズル

"""
最小回数を求めよ
3 3
1 0 2
4 5 3
7 8 6 なら

1 2 0
4 5 3
7 8 6

1 2 3
4 5 0
7 8 6

1 2 3
4 5 6
7 8 0 で3回

全ての数字が所定の場所にいる
回数無視でまずはどうすれば行けるか
任意の回数行えるなら、各数字は好きな場所に行ける

1 3
2 0 の場合

1 0
2 3

0 1
2 3

2 1
0 3

2 1
3 0

3 2 1がぐるぐる回るだけだから永遠に無理
最小操作数が24回以内なので絶対に成功するケースのみ出る

全探索4 * 24　無理
戻る必要はないので3 ** 24
多分全探索なんだろう
一つの行動で最大1合わせることができる
枝刈りする

ngはマンハッタン距離で持つ
"""

H, W = getNM()
C = [getList() for i in range(H)]

def manh(point):
    ny = (point - 1) // W
    nx = (point - 1) % W
    return ny, nx

ng = 0
sta = [0, 0]
for i in range(H):
    for j in range(W):
        if C[i][j] == 0:
            sta = [i, j]
            continue
        ny, nx = manh(C[i][j])
        ng += abs(ny - i) + abs(nx - j)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

memo = {}
ans = float('inf')

def dfs(turn, array, y, x, direct, ng):
    global ans
    if str(array) in memo and memo[str(array)] <= turn:
        return

    if ng == 0:
        ans = min(ans, turn)
        return

    if turn > 24 - ng or ans <= turn:
        return

    for i in range(4):
        if i == (direct + 2) % 4:
            continue
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < H and 0 <= nx < W:
            new_array = deepcopy(array)
            new_ng = ng
            # 0と入れ替える数字について
            my, mx = manh(array[ny][nx])
            new_ng -= (abs(my - ny) + abs(mx - nx))
            new_ng += (abs(my - y) + abs(mx - x))

            new_array[ny][nx] = array[y][x] # 0
            new_array[y][x] = array[ny][nx]
            dfs(turn + 1, new_array, ny, nx, i, new_ng)

    memo[str(array)] = turn

dfs(0, C, sta[0], sta[1], float('inf'), ng)
print(ans)

# ABC195 E - Lucky 7 Battle

"""
7の倍数　法則性なし 10とは互いに素なのでmod算をする
Siか0かをぶち込む　ここにゲーム性
7の倍数であれば高橋くんの勝ち
5 modは5
50: 5 * 10 % 7 = 1
500: 1 * 10 % 7 = 3

現在の数字: 0
これを *= 10してmod 7するか+=Si and *= 10してmod 7するか
一番最後の人が有利そう
ゲーム木みたいなやつ　逆からやっていく
0 ~ 9のdp
最後の人に0で回ってくると勝利
[[[0, 3], [3, 6], [6, 2], [2, 5], [5, 1], [1, 4], [4, 0]],
 [[0, 5], [3, 1], [6, 4], [2, 0], [5, 3], [1, 6], [4, 2]]]
高橋くんは2つ目に0 or 3で回ってくると勝利
勝利するように誘導したい
青木くんは0を受け取ると0のまま or 3で回せる

[[[0, 1], [3, 4], [6, 0], [2, 3], [5, 6], [1, 2], [4, 5]],
 [[0, 2], [3, 5], [6, 1], [2, 4], [5, 0], [1, 3], [4, 6]],
 [[0, 3], [3, 6], [6, 2], [2, 5], [5, 1], [1, 4], [4, 0]],
 [[0, 4], [3, 0], [6, 3], [2, 6], [5, 2], [1, 5], [4, 1]],
 [[0, 5], [3, 1], [6, 4], [2, 0], [5, 3], [1, 6], [4, 2]]]

5番目では0 or 3が来ると勝利　そうさせないよう
最後の人がどちらか
"""

N = getN()
S = list(input())
X = list(input())

# dp[i][j][0]: 0を追加する場合
# dp[i][j][1]: Siを追加する場合
dp = [[[0, 0] for _ in range(7)] for i in range(N)]
for i in range(N):
    for j in range(7):
        dp[i][j][0] = j * 10 % 7
        dp[i][j][1] = (j * 10 + int(S[i])) % 7

end = [0] * 7
end[0] = 1
dp.append(end)

for i in range(N - 1, -1, -1):
    # 青木
    if X[i] == 'A':
        for j in range(7):
            # 行先があれば
            if dp[i + 1][dp[i][j][0]] == 0 or dp[i + 1][dp[i][j][1]] == 0:
                dp[i][j] = 0 # lose
            else:
                dp[i][j] = 1 # win
    # 高橋
    else:
        for j in range(7):
            if dp[i + 1][dp[i][j][0]] == 0 and dp[i + 1][dp[i][j][1]] == 0:
                dp[i][j] = 0 # lose
            else:
                dp[i][j] = 1 # win

if dp[0][0] == 1:
    print('Takahashi')
else:
    print('Aoki')

# ARC085 D - ABS

N, Z, W = getNM()
A = getList()
memo = [{}, {}]

# 現在の番、最後に取られたindex
def dfs(t, ind):
    global Z, W
    if ind == N - 1:
        return abs(Z - W)

    if ind in memo[t]:
        return memo[t][ind]

    if t == 0:
        n_z = Z
        res = -float('inf')
        for i in range(ind + 1, N):
            Z = A[i]
            res = max(res, dfs(1, i))
            Z = n_z
    else:
        n_w = W
        res = float('inf')
        for i in range(ind + 1, N):
            W = A[i]
            res = min(res, dfs(0, i))
            W = n_w

    memo[t][ind] = res
    return res

print(dfs(0, -1))
