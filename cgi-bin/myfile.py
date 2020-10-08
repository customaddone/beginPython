def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

N, M = getNM()
B = [getList() for i in range(N)]
S = [getList() for i in range(M)]

# どの大きい塔からどの大きい塔へいけるように
# Unionfindかmaxflowか

def cnt(x1, y1, x2, y2, c1, c2):
    if c1 == c2:
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    else:
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) * 10

dist1 = [[float('inf')] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        x1, y1, c1 = B[i]
        x2, y2, c2 = B[j]
        dist1[i][j] = cnt(x1, y1, x2, y2, c1, c2)
dist2 = [[float('inf')] * M for i in range(M)]
for i in range(M):
    for j in range(M):
        x1, y1, c1 = S[i]
        x2, y2, c2 = S[j]
        dist2[i][j] = cnt(x1, y1, x2, y2, c1, c2)

def warshall_floyd(dist, n):
    for k in range(n):
        # i:start j:goal k:中間地点でループ回す
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

warshall_floyd(dist1, N)
warshall_floyd(dist2, M)
d1_2 = [[float('inf')] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        x1, y1, c1 = B[i]
        x2, y2, c2 = S[j]
        d1_2[i][j] = cnt(x1, y1, x2, y2, c1, c2)

for b1 in range(N):
    for b2 in range(N):
        for s1 in range(M):
            for s2 in range(M):
                dist1[b1][b2] = min(dist1[b1][b2], d1_2[b1][s1] + dist2[s1][s2] + d1_2[b2][s2])

warshall_floyd(dist1, N)

print(dist1)
