# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d
import sys
sys.setrecursionlimit(100000)

m = int(input())
n = int(input())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0

def dfs(x, y, depth):
    global ans
    maze[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] == 1:
            dfs(nx, ny, depth + 1)
    maze[y][x] = 1
    ans = max(ans, depth)
for i in range(m):
    for j in range(n):
        if maze[j][i] == 1:
            dfs(i, j, 1)
# TLEにならないんですかこれ
print(ans)
