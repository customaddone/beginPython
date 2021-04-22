import sys
sys.setrecursionlimit(10 ** 7)

def SCC(v, e):
    def DFS(x):
        visited[x] = 1
        for i in e[x]:
            if visited[i]:
                continue
            DFS(i)
        stack.append(x)

    def DFS2(x, k):
        visited[x] = 1
        res[k].append(x)
        for i in erev[x]:
            if visited[i]:
                continue
            DFS2(i, k)

    res = {}
    stack = []
    visited = [0] * v
    for i in range(v):
        if visited[i]:
            continue
        DFS(i)

    erev = [[] for _ in range(v)]
    for i in range(v):
        for j in e[i]:
            erev[j].append(i)

    visited = [0] * v
    k = 0
    while stack:
        now = stack.pop()
        if visited[now]:
            continue
        k += 1
        res[k] = []
        DFS2(now, k)

    return res

n, m = map(int, input().split())
e = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    e[a].append(b)
ans = SCC(n, e)

print(len(ans))
for j in ans.values():
    print(len(j), *j)
