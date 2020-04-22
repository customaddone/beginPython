from collections import deque

h, w = map(int, input().split())
maze = []
for i in range(h):
    s = input()
    maze.append(list(s))
ans = 0

def mazemax(px, py):
    dp = [[-1] * w for i in range(h)]
    dp[0][0] = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    pos = deque([[px, py]])

    while len(pos) > 0:
        x, y = pos.popleft()
        maze[x][y] = "#"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and maze[nx][ny] == "." and dp[nx][ny] == -1:
                dp[nx][ny] = dp[x][y] + 1
                pos.append([nx, ny])
    for i in range(w):
        for j in range(h):
            ans = max(ans, dp[i][j])


for i in range(w):
    for j in range(h):
        if maze[i][j] == ".":
            mazemax(i, j)
print(ans)
