# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f
from collections import deque
import heapq
INF = 10 ** 20

# n: 街の数
# m: 道路の数
# k: ゾンビ占領地域
# s: ゾンビの行動範囲
N, M, K, S = map(int,input().split())
# それぞれ安全な街、危険な街での宿泊料
P,Q = map(int,input().split())

# ゾンビ占領地域
zombie = []
for k in range(K):
    zombie.append(int(input()) - 1)

# 道リスト
link = [ [] for _ in range(N)]

for m in range(M):
    a, b = map(int, input().split())
    link[a - 1].append(b - 1)
    link[b - 1].append(a - 1)

dist = [INF] * N
q = deque(zombie)
# ゾンビ占領地域はinf → 0
for v in zombie:
    dist[v] = 0
while q:
    node = q.popleft()
    for next in link[node]:
        if dist[next] != INF:
            continue
        # ゾンビの出発先 = ゾンビの出発元 + 1
        dist[next] = dist[node] + 1
        q.append(next)

cost = [P] * N
for n in range(N):
    # infじゃなければ
    if dist[n] <= S:
        cost[n] = Q
    if n in zombie:
        cost[n] = INF
    if n == 0 or n == N - 1:
        # 最初と最後は宿泊料いらない
        cost[n] = 0

# startとgoal
def dijkstra(s, g):
    dists  = [INF for i in range(N)]
    dists[s] = 0
    pq = [(0, s)]
    # (0, s)の後ろの部分がgになったら
    while(pq[0][1] != g):
        # heapqは最小値を取り出す時に圧倒的に速い
        # ダイクストラで使える
        d, node = heapq.heappop(pq)
        if (d > dists[node]):
            continue
        for next in link[node]:
            # nextに行くためにかかるコスト
            c = cost[next]
            if d + c < dists[next]:
                dists[next] = d + c
                heapq.heappush(pq, (dists[next], next))
    return pq[0][0]
print (dijkstra(0, N - 1))
