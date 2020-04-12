from copy import deepcopy
ans = 1000000
# dfsを完全に理解してしまったかもしれない
def dfs(now, ignore):
    if len(ignore) == n:
        print(ignore)
    for i in dist[now]:
        if i in ignore:
            continue
        nignore = deepcopy(ignore)
        nignore.append(i)
        dfs(i, nignore)

n = 8
dist = [
        [1, 2, 4],
        [0, 3, 8],
        [0, 5],
        [1, 7, 8],
        [0, 8],
        [6, 8],
        [5, 7],
        [3, 6],
        [1, 3, 4, 5]
       ]
dfs(0, [0])
