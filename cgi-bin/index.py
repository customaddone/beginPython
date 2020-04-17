def dij(edges, num_v):
    dist = [float('inf') for i in range(num_v)]
    dist[0] = 0
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

edges = [
         [[1, 4], [2, 3], [3, 9]],
         [[0, 4], [2, 9]],
         [[0, 3], [1, 9], [3, 2], [4, 5]],
         [[0, 9], [2, 2], [4, 1]],
         [[2, 5], [3, 1]]
         ]
print(dij(edges, 5))
