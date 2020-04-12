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

# これ
pos = deque([[8, 8, 0]])

while len(pos) > 0:
    x, y, depth = pos.popleft()
    if maze[x][y] == 1:
        print(depth)
    maze[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] < 2:
            pos.append([nx, ny, depth + 1])
