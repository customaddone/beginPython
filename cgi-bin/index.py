n = int(input())
cnt = 0

list = [i for i in range(1,n + 1)]
for i in list:
    if len(str(i)) % 2 == 1:
        cnt += 1
print(cnt)
