tree = [[1, 2], [3, 4], [5, 6],[7, 8]]

data = [0]
while len(data) > 0:
    pos = data.pop(0)
    print(pos, end="")
    for i in tree[pos]:
        data.append(i)
