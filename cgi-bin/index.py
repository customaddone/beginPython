from collections import deque

s = deque(input())
q = int(input())
counter = 1
lista = [list(input().split()) for i in range(q)]

def rever(i):
    if i == '1':
        return 1
    else:
        return -1
for i in lista:
    if i[0] == '1':
        counter = -1 * counter
    else:
        if counter * rever(i[1]) > 0:
            s.appendleft(i[2])
        else:
            s.append(i[2])
s = "".join(list(s))
if counter > 0:
    print(s)
else:
    print(s[::-1])
