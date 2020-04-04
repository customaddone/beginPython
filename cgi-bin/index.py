def bellman_ford(edges, num_v):
    dist = [float('inf') for i in range(num_v)]
    dist[0] = 0

    changed = True
    while changed:
        changed = False
        # roop1
        # edge1 [0, 1, 4]
        # edge2 [0, 2, 3]
        # ...
        # edge9 [5, 6, 4]

        # 変更があったので最初からfor edge in edges:する
        for edge in edges:
            # dist[edge[1]]:終点 dist[edge[0]]:始点 edge[2]:コスト
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                changed = True
    return dist

edges = [[0,1,4],[0,2,3],[1,2,1],[1,3,1],[1,4,5],[2,5,2],[4,6,2],[5,4,1],[5,6,4]]
print(bellman_ford(edges,7))
