#############
# Main Code #
#############

A, B = map(int, input().split())
num = [-10, -5, -1, 1, 5, 10]

# 解法1
dp = [[0] * 41 for i in range(41)]
dp[0][A] = 1

if A == B:
    print(0)
    exit()

for i in range(1, 41):
    for j in range(41):
        for l in range(len(num)):
            if 0 <= j - num[l] <= 40:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - num[l]])
        if dp[i][B] >= 1:
            print(i)
            exit()

'''
解法2
pos = deque([[A, 0]])

while pos[0][0] != B:
    u, cnt = pos.popleft()
    for i in num:
        if 0 <= u + i <= 40:
            pos.append([u + i, cnt + 1])

print(pos[0][1])

解法3
dist = [[] for i in range(41)]
for i in range(41):
    for j in num:
        if 0 <= i + j <= 40:
            dist[i].append([i + j, 1])

N = 41
def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        d, now = heapq.heappop(pq)
        if (d > dist[now]):
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                heapq.heappush(pq, (dist[i[0]], i[0]))
    return dist

print(dij(A, dist)[B])
'''
