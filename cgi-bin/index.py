def dijkstra(edges, num_v):
    # 各頂点をinfに
    dist = [float('inf')] * num_v
    # 始点を解放
    dist[0] = 0
    # 各頂点に番号を振る
    q = [i for i in range(num_v)]

    while len(q) > 0:
        # qの先頭
        r = q[0]
        # 最もコストが小さい頂点を探す
        for i in q:
            if dist[i] < dist[r]:
                r = i

        # 最もコストが小さい頂点を取り出す
        # 一番コストが小さい頂点から頂点xに飛べるか
        u = q.pop(q.index(r))
        # edges[u]1: [1, 4]
        # edges[u]2: [2, 3]
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                dist[i[0]] = dist[u] + i[1]

    return dist

edges=[[[1,4],[2,3]],
[[2,1],[3,1],[4,5]],
[[5,2]],
[[4,3]],
[[6,2]],
[[4,1],[6,4]],
[]]

print(dijkstra(edges,7))
