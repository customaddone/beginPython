# https://atcoder.jp/contests/abc079/tasks/abc079_d
n, w = map(int, input().split())

dist = [[float('inf')] * 10 for i in range(10)]
for i in range(10):
    c = list(map(int, input().split()))
    for j in range(10):
        dist[i][j] = c[j]

# warshall_floydを回してdistを改良
def warshall_floyd(dist):
    for k in range(10):
        # i:start j:goal k:中間地点でループ回す
        for i in range(10):
            for j in range(10):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
warshall_floyd(dist)

board = [list(map(int, input().split())) for i in range(n)]

cnt = 0
for row in board:
    for i in row:
        if (i == -1) or (i == 1):
            continue
        else:
            cnt += dist[i][1]
print(cnt)
