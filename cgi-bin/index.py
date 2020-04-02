pos = [[1, 1, 0]]

def search(x, y, depth):
    if maze[x][y] == 1:
        print(depth)
        exit()

    maze[x][y] = 2

    if maze[x - 1][y] < 2:
        search(x - 1, y, depth + 1)
    if maze[x + 1][y] < 2:
        search(x - 1, y, depth + 1)
    if maze[x][y - 1] < 2:
        search(x, y - 1, depth + 1)
    if maze[x][y + 1] < 2:
        search(x, y + 1, depth + 1)

    # 詰まったら元にもどす
    maze[x][y] = 0

search(1, 1, 0)
