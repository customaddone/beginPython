from collections import deque
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
    if x == gx and y == gy:
        break
    maze[x][y] = '#'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] == "." and dp[nx][ny] == -1:
            pos.append([nx, ny, depth + 1])
            dp[nx][ny] = dp[x][y] + 1
print(dp[gx][gy])
