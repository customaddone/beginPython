# https://atcoder.jp/contests/abc151/tasks/abc151_d
from collections import deque
from copy import deepcopy

h, w = map(int, input().split())
mazemother = []
# 入力の仕方を変えるとxとyを逆にしなくて良くなる？
for i in range(h):
    s = input()
    mazemother.append(list(s))
ans = 0

def mazemax(px, py):
    global ans
    # deepcopyしないとmazeが狂う
    maze = deepcopy(mazemother)
    dp = [[-1] * w for i in range(h)]
    # dp, mazeは全てxとyを逆にしておく
    dp[py][px] = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    pos = deque([[px, py]])

    while len(pos) > 0:
        x, y = pos.popleft()
        maze[y][x] = "#"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] == "." and dp[ny][nx] == -1:
                dp[ny][nx] = dp[y][x] + 1
                pos.append([nx, ny])
    for i in range(w):
        for j in range(h):
            ans = max(ans, dp[j][i])


for i in range(w):
    for j in range(h):
        if mazemother[j][i] == ".":
            mazemax(i, j)
print(ans)
