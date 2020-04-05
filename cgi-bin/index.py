import sys
# 再帰制限を外す
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
c = [list(input()) for i in range(n)]

# 到達したかどうか（0は未到達、1は到達済み）
d = [[0] * m for i in range(n)]

# 移動する4方向
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    d[x][y] = 1

    # 移動４方向をループ
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m and d[nx][ny] == 0 and c[nx][ny] != "#":
            dfs(nx, ny)

# スタートはどこ？
for i in range(n):
    for j in range(m):
        if c[i][j] == "s":
            dfs(i, j)
for i in range(n):
    for j in range(m):
        if c[i][j] == "g" and d[i][j]:
            print("Yes")
            exit()
print("No")
