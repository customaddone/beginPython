# https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_e
from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.buffer.readline

INF = 10 ** 10
n, k = map(int,input().split())
C = []
R = []
for _ in range(n):
    c, r =map(int,input().split())
    C.append(c)
    R.append(r)
edges = [[] for _ in range(n)]
for _ in range(k):
    a, b = map(int,input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

d = [[INF] * n for _ in range(n)]
for i in range(n):
    q = deque([i])
    d[i][i] = 0
    while q:
        cur = q.popleft()
        for to in edges[cur]:
            if d[i][to] < INF:
                continue
            d[i][to] = d[i][cur] + 1
            q.append(to)

for i in range(n):
    c, r = C[i], R[i]
    for j in range(n):
        if d[i][j] <= r:
            d[i][j] = c
        else:
            d[i][j] = INF
del edges, C, R

def dijkstra(s,e):
    ds = [INF] * n
    used = [False] * n
    ds[s] = 0

    for _ in range(n):
        v = -1
        for i in range(n):
            if used[i]:
                continue
            if v == -1:
                v = i
            elif ds[i] < ds[v]:
                v = i
        if v == -1:
            break
        used[v] = True
        for nv in range(n):
            ds[nv] = min(ds[nv], ds[v] + d[v][nv])
    return ds[e]

print(dijkstra(0,n-1))
