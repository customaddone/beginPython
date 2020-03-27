s = int(input())
list = []
while not(s in list):
    list.append(s)
    if s % 2 == 0:
        s /= 2
    else:
        s = 3 * s + 1
print(len(list) + 1)
