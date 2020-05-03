# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja
n, w = map(int, input().split())

dist = [[float('inf')] * n for i in range(n)]
for i in range(n):
    dist[i][i] = 0
for i in range(w):
    x, y, z = map(int, input().split())
    dist[x][y] = z

def warshall_floyd(dist):
    for k in range(n):
        # i:start j:goal k:中間地点でループ回す
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
print(warshall_floyd(dist))
