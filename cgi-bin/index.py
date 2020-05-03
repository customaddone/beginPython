# https://atcoder.jp/contests/abc012/tasks/abc012_4
n, w = map(int, input().split())

dist = [[float('inf')] * n for i in range(n)]
for i in range(n):
    dist[i][i] = 0
for i in range(w):
    x, y, z = map(int, input().split())
    dist[x - 1][y - 1] = z
    dist[y - 1][x - 1] = z

def warshall_floyd(dist):
    for k in range(n):
        # i:start j:goal k:中間地点でループ回す
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

warshall_floyd(dist)

ans = float('inf')
for i in dist:
    opt = max(i)
    ans = min(ans, opt)
print(ans)
