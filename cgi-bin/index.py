from copy import deepcopy
import collections
# dfsを完全に理解してしまったかもしれない
pos = collections.deque([[0, [0]]])
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
       
while len(pos) > 0:
    now, ignore = pos.popleft()
    if len(ignore) == n:
        print(ignore)
    for i in dist[now]:
        if i in ignore:
            continue
        nignore = deepcopy(ignore)
        nignore.append(i)
        pos.append([i, nignore])
