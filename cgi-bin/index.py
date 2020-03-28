n, x, y = map(int, input().split())
anslist = [0] * n
list = []
for m in range(1, n + 1):
    for n in range(m, n + 1):
        if m != n:
            list.append([m, n])
while len(list) != 0:
    dis = list[0][1] - list[0][0]
    warpdis = (abs(x - list[0][0])) + (abs(list[0][1] - y)) + 1
    anslist[min(dis, warpdis)] += 1
    list.pop(0)
for i in range(1, n):
    print(anslist[i])
