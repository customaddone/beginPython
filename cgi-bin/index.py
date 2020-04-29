# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja
from collections import deque

n = int(input())
dist = [[] for i in range(n)]
for i in range(n):
    d = list(map(int, input().split()))
    if len(d) > 2:
        # 2文字目以降をappend
        for j in d[2:]:
            dist[i].append(j - 1)
ignore = [0] * n
ignore[0] = 1
pos = deque([[0, 0]])
dp = [0] * n

while len(pos) > 0:
    u, depth = pos.popleft()
    dp[u] = depth
    for i in dist[u]:
        if ignore[i] == 0:
            pos.append([i, depth + 1])
            ignore[i] = 1
            
for i in range(n):
    print(i + 1, end = " ")
    print(dp[i])
