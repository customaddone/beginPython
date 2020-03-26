input()
list = list(map(int, input().split()))
counter = 0
while 1:
    if all([i % 2 == 0 for i in list]):
        list = [int(i / 2) for i in list]
        counter += 1
    else:
        break
print(counter)
