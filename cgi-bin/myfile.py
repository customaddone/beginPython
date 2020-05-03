def dijkstra(s, n, cost):#スタート, 頂点数, cost[s][t]:辺stのコスト（存在しなければinf）
    inf = 10**18
    dist = [inf] * n
    used = [False] * n
    dist[s] = 0
    for _ in range(n):
        v = -1
        for i in range(n):
            if used[i]:
                continue
            if v == -1:
                v = i
            elif dist[i]<dist[v]:
                v = i
        if v == -1:
            break
        used[v] = True
        for nv in range(n):
            dist[nv] = min(dist[nv], dist[v]+cost[v][nv])
    return dist[-1]
print (dij(0, 4))
