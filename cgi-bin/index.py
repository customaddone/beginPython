import sys
from copy import deepcopy
sys.setrecursionlimit(10 ** 9)

n = int(input())
lista = [[] for i in range(n + 1)]
ans = float('inf')
for i in range(n):
    a = int(input())
    lista[i + 1].append(a)
def dfs(now, ignore):
    global ans
    if now == 2:
        ans = min(ans, len(ignore) - 1)
    for i in lista[now]:
        if i in ignore:
            continue
        nignore = deepcopy(ignore)
        nignore.append(i)
        dfs(i, nignore)
dfs(1, [1])
print(-1 if ans == float('inf') else ans)
