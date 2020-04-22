from collections import deque
h, w = map(int, input().split())
maze = [list(input()) for i in range(h)]
dp = [[-1] * w for i in range(h)]
dp[2][0] = 0
pos = deque([[0, 2]])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while len(pos) > 0:
    x, y = pos.popleft()
    maze[y][x] = '#'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] =='.' and dp[ny][nx] == -1:
            dp[ny][nx] = dp[y][x] + 1
            pos.append([nx, ny])
print(dp)
