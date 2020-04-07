import sys
sys.setrecursionlimit(1000000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    d[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # dは行った場所のメモ　cは実際の地形
        if 0 <= nx < n and 0 <= ny < m and d[nx][ny] == 0 and c[nx][ny] != "#":
            dfs(nx, ny)
