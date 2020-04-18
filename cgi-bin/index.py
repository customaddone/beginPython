from copy import deepcopy

def dfs(now, ignore, sumtime):
    global ans
    if len(ignore) == n:
        ans = min(ans, sumtime)
    for i in dist[now]:
        if i[0] in ignore:
            continue
        nignore = deepcopy(ignore)
        nignore.append(i[0])
        dfs(i[0], nignore, sumtime + i[1])

n = 4
ans = 1000000
# 通行止めをした
dist = [
        [[1, 8], [2, 7], [3, 3]],
        [[0, 8], [2, 9]],
        [[0, 7], [1, 9], [3, 4]],
        [[0, 3], [2, 4]]
       ]

for i in range(n):
    dfs(i, [i], 0)
print(ans)
