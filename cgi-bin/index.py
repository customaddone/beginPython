n = int(input())
sum = 0
for _ in range(n):
    x, u = input().split()
    if u == 'JPY':
        sum += int(x)
    else:
        # *はfloatの内側
        sum += float(x) * 38000
print(sum)
