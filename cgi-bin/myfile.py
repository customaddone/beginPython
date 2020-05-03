# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f
from collections import deque
import heapq
# 用意しとく
inf = 10 ** 20

# n: 街の数
# m: 道路の数
# k: ゾンビ占領地域
# s: ゾンビの行動範囲
n, m, k, s = map(int, input().split())
# それぞれ安全な街、危険な街での宿泊料
p, q = map(int, input().split())
# ゾンビ占領地域
zombie = []
for i in range(k):
    zombie.append(int(input())-1)
# 道リスト
link = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    link[a - 1].append(b - 1)
    link[a - 1].append(a - 1)

dist = [inf] * n
q = deque(zombie)

# ゾンビ占領地域はinf → 0
for v in zombie:
    dist[v] = 0
while q:
    node = q.popleft()
    for next in link[node]:
        if dist[next] != inf:
            continue
        # ゾンビの出発先 = ゾンビの出発元 + 1
        dist[next] = dist[node] + 1
        q.append(next)

cost = [p] * n
for i in range(n):
    # infじゃなければ
    if dist[i] <= s:
        cost[i] = q
    if n in zombie:
        cost[i] = inf
    # 最初と最後は宿泊料いらない
    if i == 0 or i == n - 1:
        cost[i] = 0
# startとgoal
def dij(s, g):
    dist = [inf for i in range(n)]
    dist[s] = 0
    pq = [(0, s)]
    # (0, s)の後ろの部分がgになったら
    while (pq[0][1] != g):
        d, node = heapq.heappop(pq)
        print([d, node])
        if (d > dist[node]):
            continue
        for next in link[node]:
            # nextに行くためにかかるコスト
            c = cost[next]
            if d + c < dist[next]:
                dist[next] = d + c
                heapq.heappush(pq, (dist[next], next))
    return pq[0][0]
print (dij(0, n - 1))
