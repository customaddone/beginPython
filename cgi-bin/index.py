import collections
from copy import deepcopy
dist = [
        [1, 2, 4],
        [0, 3, 4, 8],
        [0, 5],
        [1, 7, 8],
        [0, 1, 8],
        [2, 6, 8],
        [5, 7],
        [3, 6],
        [1, 3, 4, 5]
        ]
pos = collections.deque([[0, [0]]])

while len(pos) > 0:
    now, ignore = pos.popleft()
    if now == 6:
        print(ignore)
    for i in dist[now]:
        if i in ignore:
            continue
        nignore = deepcopy(ignore)
        nignore.append(i)
        pos.append([i, nignore])
