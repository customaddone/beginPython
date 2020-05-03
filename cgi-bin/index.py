# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja#
v, e, r = map(int, input().split())
edges = [[] for i in range(v)]
for i in range(e):
    s, t, d = map(int, input().split())
    edges[s].append([t, d])
    # この問題は双方向ではない
    # edges[t].append([s, d])

def dij(edges, num_v, start):
    dist = [float('inf')] * num_v
    dist[start] = 0
    q = [i for i in range(num_v)]

    while len(q) > 0:
        r = q[0]
        for i in q:
            if dist[i] < dist[r]:
                r = i
        u = q.pop(q.index(r))
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                dist[i[0]] = dist[u] + i[1]
    return dist
for i in dij(edges, v, r):
    print(i)
