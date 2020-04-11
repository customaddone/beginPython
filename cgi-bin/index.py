from copy import deepcopy

def dfs(now, ignore, sumtime):
    if len(ignore) == n:
        print(sumtime)
    for i in dist[now]:
        if i[0] in ignore:
            continue
        nignore = deepcopy(ignore)
        nignore.append(i[0])
        dfs(i[0], nignore, sumtime + i[1])

n = 3
ans = 1000000
dist = [[[1, 5], [2, 2]], [[0, 5], [2, 4]], [[0, 2], [1, 4]]]

dfs(0, [0], 0)
