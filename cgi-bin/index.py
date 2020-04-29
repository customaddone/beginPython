from collections import deque

h, w, n = map(int, input().split())
maze = []
for i in range(h):
    a = input()
    maze.append(list(a))
# スタート位置特定
start = [-1, -1]
# 寄り道はしないように
dp = [[-1] * (w + 1) for i in range(h + 1)]
dp[start[1]][start[0]] = 0
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
# 第一、第二引数が座標
# 第三引数が経過時間
# 第四引数が訪れた工場の数
pos = deque([[start[0], start[1], 0, 1]])
maze[start[1]][start[0]] = '.'

while len(pos) > 0:
    x, y, time, factcnt = pos.popleft()
    if factcnt == n + 1:
        print(time)
        break
    # dp[y][x]を訪れるまでにいくつチーズを食べたか
    dp[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 1 ~ 9の工場を巡回する（体力は考慮しなくていい）
        if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] != 'X' and dp[ny][nx] == -1:
            if maze[ny][nx] == str(factcnt):
                # チーズ工場を破壊
                maze[ny][nx] = "."
                # 一回dequeとdpをリセット
                pos = deque([])
                dp[ny][nx] = 0
                dp = [[-1] * (w + 1) for i in range(h + 1)]
                pos.append([nx, ny, time + 1, factcnt + 1])
                # forループから抜ける
                break
            else:
                pos.append([nx, ny, time + 1, factcnt])
