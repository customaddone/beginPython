def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

H, W, T = getNM()
maze = [list(input()) for _ in range(H)]

minT = 0
maxT = 10 ** 9 + 1

start = []
goal = []
for i in range(H):
    for j in range(W):
        if maze[i][j] == "S":
            start = [i,j]
        if maze[i][j] == "G":
            goal = [i,j]

def comp_dist(x, s):
    return x if s == "#" else 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dij(start_x, start_y, goal_x, goal_y, dis):
    dist = [[float("inf") for _ in range(W)] for _ in range(H)]
    dist[start_y][start_x] = 0
    pq = [(0, start_x, start_y)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while (pq[0][1] != goal_x or pq[0][2] != goal_y):
        distance, x, y = heapq.heappop(q)

        if distance > dist[y][x]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < W and 0 <= ny < H:
                nd = dist[y][x] + comp_dist(dis, maze[ny][nx])
                if dist[ny][nx] > nd:
                    dist[ny][nx] = nd
                    heapq.heappush(pq, [dist[ny][nx], nx, ny])
    return pq[0][0]

print(dij(0, 0, 2, 1, 1))
