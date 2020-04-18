from collections import deque
maze = [
    [9,9,9,9,9,9,9,9,9,9],
    [9,0,9,0,0,0,0,9,1,9],
    [9,0,9,0,9,0,0,0,0,9],
    [9,0,0,0,9,0,9,9,0,9],
    [9,9,0,9,9,0,0,0,9,9],
    [9,0,0,0,9,9,9,0,9,9],
    [9,0,9,0,0,0,0,0,9,9],
    [9,0,0,0,9,0,9,0,0,9],
    [9,0,0,0,0,0,0,0,0,9],
    [9,9,9,9,9,9,9,9,9,9]
]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dp = [[-1] * 10 for i in range(10)]
dp[1][1] = 0

# これ
pos = deque([[1, 1, 0]])

while len(pos) > 0:
    x, y, depth = pos.popleft()
    if maze[x][y] == 1:
        print(dp[x][y])
        break
    maze[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] < 2 and dp[nx][ny] == -1:
            pos.append([nx, ny, depth + 1])
            dp[nx][ny] = dp[x][y] + 1
