from collections import deque

h, w = map(int, input().split())
maze = []
for i in range(h):
    s = input()
    maze.append(list(s))
# 最短経路の道筋以外は全て黒にしていい
# dotの数の合計-スタートからゴールまでの最短経路で答えを求める
dotsum = 0
for row in maze:
    for j in row:
        if j == ".":
            dotsum += 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dp = [[-1] * (w + 1) for i in range(h + 1)]
dp[0][0] = 0

pos = deque([[0, 0, 0]])
dotroute = 0

while len(pos) > 0:
    x, y, depth = pos.popleft()
    if x == w - 1 and y == h - 1:
        dotroute = depth + 1
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] == "." and dp[ny][nx] == -1:
            dp[ny][nx] = dp[y][x] + 1
            pos.append([nx, ny, depth + 1])
if dotroute == 0:
    print(-1)
else:
    print(dotsum - dotroute)
