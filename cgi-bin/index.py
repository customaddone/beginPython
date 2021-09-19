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

# ARC005 C - 器物損壊！高橋君

H, W = getNM()
maze = [list(input()) for i in range(H)]

for i in range(H):
    for j in range(W):
        if maze[i][j] == 's':
            si = [i, j]
            maze[i][j] = '.'
        elif maze[i][j] == 'g':
            gi = [i, j]
            maze[i][j] = '.'

pos = deque([[si[0], si[1]]])
dist = [[-1] * W for j in range(H)]
dist[si[0]][si[1]] = 0

# 0-1bfs
while pos:
    y, x = pos.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < H and 0 <= nx < W and dist[ny][nx] == -1:
            if maze[ny][nx] == '.':
                dist[ny][nx] = dist[y][x]
                pos.appendleft([ny, nx])
            else:
                dist[ny][nx] = dist[y][x] + 1
                pos.append([ny, nx])

if dist[gi[0]][gi[1]] <= 2:
    print('YES')
else:
    print('NO')

# ABC007 幅優先探索
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gx, gy = map(int, input().split())
sy -= 1
sx -= 1
gx -= 1
gy -= 1

maze = []
ans = float('inf')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

pos = deque([[sx, sy, 0]])
dp = [[-1] * (c + 1) for i in range(r + 1)]
dp[sx][sy] = 0

for i in range(r):
    c = input()
    maze.append(list(c))

while len(pos) > 0:
    x, y, depth = pos.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] == "." and dp[nx][ny] == -1:
            pos.append([nx, ny, depth + 1])
            dp[nx][ny] = dp[x][y] + 1
print(dp[gx][gy])

# ABC176 D - Wizard in Maze
H, W = getNM()
Ch, Cw = getNM()
Dh, Dw = getNM()
maze = [input() for i in range(H)]
Ch -= 1
Cw -= 1
Dh -= 1
Dw -= 1

# ワープを最低で何回使うか
# 上下左右2つ向こうまでの範囲内でワープできる
# 隣接する'.'が領域

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

pos = deque([[Ch, Cw]])
dp = [[-1] * W for i in range(H)]
dp[Ch][Cw] = 0

while len(pos) > 0:
    y, x = pos.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 歩いて移動
        if 0 <= nx < W and 0 <= ny < H and maze[ny][nx] == "." and (dp[ny][nx] == -1 or dp[y][x] < dp[ny][nx]):
            # 0-1 bfs
            # 先頭に置く
            pos.appendleft([ny, nx])
            dp[ny][nx] = dp[y][x]
    # ワープ
    for i in range(-2, 3):
        for j in range(-2, 3):
            wy = y + i
            wx = x + j
            # 歩いて移動不可能でないと使わない
            if 0 <= wx < W and 0 <= wy < H and maze[wy][wx] == "." and dp[wy][wx] == -1:
                pos.append([wy, wx])
                dp[wy][wx] = dp[y][x] + 1

print(dp[Dh][Dw])

# AGC033 A - Darker and Darker

"""
一番近い#までの距離
100万マスあるので一回の探索で済むように
黒マスの周囲４マスを探索
用が済めばポイ　同じマスについて探索する必要はない
これで計算量は4 * H * W
"""

H, W = getNM()
maze = [list(input()) for i in range(H)]
prev = []
for i in range(H):
    for j in range(W):
        if maze[i][j] == '#':
            prev.append((i, j))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

flag = True
ans = 0
while flag:
    flag = False
    next = []
    while prev:
        y, x = prev.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and maze[ny][nx] == '.':
                flag = True
                maze[ny][nx] = '#'
                next.append((ny, nx))
    prev = next
    if flag:
        ans += 1

print(ans)

# AGC043 A - Range Flip Find Route

"""
白いとこだけ踏んでゴールを目指す
スタートやゴールが黒いこともある

操作をすると選択した長方形空間内の白黒が反転する
最小で何回操作するか
効率の良い操作方法を考える

黒い部分を白くすることだけを考える？
白だけ踏んでいけるとは？
二回反転させれば元どおり

白から黒に、黒から白に侵入するときだけ += 1する？
"""

H, W = getNM()
maze = [list(input()) for i in range(H)]
dp = [[float('inf')] * W for i in range(H)]
dp[0][0] = 0
if maze[0][0] == "#":
    dp[0][0] = 1

dy = [0, 1]
dx = [1, 0]

pos = deque([[0, 0]])

# 0 - 1bfs?
while pos:
    y, x = pos.popleft()
    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < H and 0 <= nx < W: # 領域内
            # 同じ色の場合
            if maze[y][x] == maze[ny][nx] and dp[ny][nx] > dp[y][x]:
                pos.appendleft([ny, nx])
                dp[ny][nx] = dp[y][x]
            # 違う色の場合
            if maze[y][x] != maze[ny][nx]:
                # 入るときだけでいい
                if maze[y][x] == "." and dp[ny][nx] > dp[y][x] + 1:
                    pos.append([ny, nx])
                    dp[ny][nx] = dp[y][x] + 1
                elif maze[y][x] == "#" and dp[ny][nx] > dp[y][x]:
                    pos.appendleft([ny, nx])
                    dp[ny][nx] = dp[y][x]

print(dp[H - 1][W - 1])

# AGC014 C - Closed Rooms

"""
H行W列
K回まで移動できる　K個の部屋を解放する
端っこの'.'を目指す　またダイクストラか

黒を移動できると考えてもいい
全探索する
端っこの部屋についての最短距離を求める
0-1bfsか

最初の１回は['.']の部分だけ移動できる
次からは['.'] + ['#']を移動できる

端っこまで黒何個消しで行けるか
単純な距離　と
黒を何個消すか　を求める

1回目白マス行けるとこまで移動する　
あとは自由に航行できる（前回のでKマス部屋を開いて今回Kマス進むため）

ほぼほぼ'#'は関係がない
posの中身を途中で書き換える問題
"""

H, W, K = getNM()
maze = [list(input()) for i in range(H)]

start = [-1, -1]
# スタート位置特定
for i in range(H):
    for j in range(W):
        if maze[i][j] == 'S':
            start = [i, j]
            break
    else:
        continue
    break

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

dis = [[-1] * W for i in range(H)]
dis[start[0]][start[1]] = 0

# 最初の１回 白マス内だけをK回まで移動する
# これらで移動したものは全てK回移動でカウントする
pos = deque([[start[0], start[1], 0]])
alta = [[start[0], start[1], K]]
while len(pos) > 0:
    y, x, d = pos.popleft()
    if d == K:
        continue
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < H and 0 <= nx < W and dis[ny][nx] == -1 and maze[ny][nx] == ".":
            dis[ny][nx] = d + 1
            alta.append([ny, nx, K])
            pos.append([ny, nx, d + 1])

ans = float('inf')
# あとはそのまま直進して壁にぶつかるだけ
for y, x, d in alta:
    up = y
    down = (H - 1) - y
    left = x
    right = (W - 1) - x
    opt = ((min(up, down, left, right) + K - 1) // K) + 1

    ans = min(ans, opt)

print(ans)

# パ研合宿2020　第2日「パ研杯2020」 B - Walking

"""
2 3
EEE
SSS

Eなら右
Sなら下　端にいくと終了

maze[0][0] ~ maze[H][W]までいけるか
maze[H][W]の文字をEにする

最小の交換
0-1 bfs
0: 右(E)
1: 下(S)
"""

H, W = getNM()
maze = [list(input()) for i in range(H)]
dp = [[-1] * (W + 1) for i in range(H + 1)]
dp[0][0] = 0

q = deque([[0, 0]])

while q:
    y, x = q.popleft()
    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        # 細工する
        if 0 <= y < H and 0 <= x < W and dp[ny][nx] == -1:
            # E and 下　or S and 右
            if (maze[y][x] == 'E') ^ (i == 0):
                dp[ny][nx] = dp[y][x] + 1 # 変更
                q.append([ny, nx])
            # 正しい方向の場合
            else:
                dp[ny][nx] = dp[y][x]
                q.appendleft([ny, nx])

print(dp[H - 1][W])

# edufo #97  D. Minimal Height Tree

"""
bfsをします
ascending order　で見ている
順番を与えられる　もっとも高さが低い木の高さは？
とにかく圧縮していく
1→2, 1→3...(スターグラフ)だと高さが一番低く、高さ1
数字が逆転している場合はここから抜く
前から順に昇順に抜いていく

1 4 2 3
1を0段目に置く
4を1段目に置く
2は４と並列には置けない　1段目のどれかの子要素として2段目に置く

例えば　1 - 4 - 3
         - 5 - 2 みたいなグラフも許される　1 4 5 3 2 は高さ2
反転は前の段の頂点数 - 1まで
"""

T = getN()
for _ in range(T):
    N = getN()
    A = getList() # 順番
    res = 1
    prev, next, rev = 1, 0, 0 # 前の段の要素の数, 現在の段の要素の数、と現在の段の反転数
    for i in range(1, N):
        # 反転している　prevの個数 - 1までは許される
        if A[i - 1] > A[i]:
            # これ以上は持てないので段を変える
            if rev + 1 == prev:
                res += 1
                prev = next # これは1以上
                rev = 0
                next = 0
            else:
                rev += 1

        # 置く
        next += 1

    print(res)
