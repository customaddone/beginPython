from collections import deque

h, w, n = map(int, input().split())
maze = []
for i in range(h):
    a = input()
    maze.append(list(a))

start = [-1, -1]
end = [-1, -1]
ans = 0
# スタート位置特定
for i in range(w):
    for j in range(h):
        if maze[j][i] == 'S':
            start = [i, j]
            break
    else:
        continue
    break
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# スタート位置破壊
maze[start[1]][start[0]] = '.'

# n → n + 1へ移動するまでにかかる時間
def bfs(sta, end):
    global start
    pos = deque([[sta[0], sta[1], 0]])
    # 寄り道はしないように
    dp = [[-1] * (w + 1) for i in range(h + 1)]
    while len(pos) > 0:
        x, y, time = pos.popleft()
        if maze[y][x] == str(end):
            start = [x, y]
            return dp[y][x] + 1
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] != 'X' and dp[ny][nx] == -1:
                # [x, y]に隣接する部分を+1していく
                # ここ重要　計算量が超減る
                dp[ny][nx] = dp[y][x] + 1
                pos.append([nx, ny, time + 1])
# 1→2 2→3...8→9の移動時間の合計
for i in range(n):
    ans += bfs([start[0], start[1]], i + 1)
print(ans)
