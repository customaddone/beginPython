maze = [
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]
        ]

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
counter = 0
def dfs(x, y, depth):
    global counter
    if depth == 25:
        counter += 1
    maze[x][y] = depth
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= 4 and 0 <= ny <= 4 and maze[nx][ny] == 0:
            dfs(nx, ny, depth + 1)
    maze[x][y] = 0
dfs(0, 0, 1)
# 計算量やばそう
print(counter)
