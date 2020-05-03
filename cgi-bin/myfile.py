from collections import deque
import heapq

num_v = 5

def dij(start, goal):
    dist = [float('inf') for i in range(num_v)]
    dist[start] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while (pq[0][1] != goal):
        d, now = heapq.heappop(pq)
        if (d > dist[now]):
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                heapq.heappush(pq, (dist[i[0]], i[0]))
    return pq[0][0]

edges = [
         [[1, 4], [2, 3], [3, 9]],
         [[0, 4], [2, 9]],
         [[0, 3], [1, 9], [3, 2], [4, 5]],
         [[0, 9], [2, 2], [4, 1]],
         [[2, 5], [3, 1]]
         ]
print (dij(0, 4))
