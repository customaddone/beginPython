# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp
w, h = map(int, input().split())
maze = [list(map(int, input().split())) for i in range(h)]
# 8方向のベクトル
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
cnt = 0
def dfs(x, y):
    global cnt
    # 陸を沈める
    maze[y][x] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] == 1:
            dfs(nx, ny)

for i in range(w):
    for j in range(h):
        if maze[j][i] == 1:
            dfs(i, j)
            cnt += 1
print(cnt)
