import collections
tree = [[1, 2], [3, 4], [5, 6],[],[],[],[]]
list = collections.deque([0])

while len(list) > 0:
    pop = list.popleft()
    print(pop, end = " ")
    for i in tree[pop]:
        list.append(i)
