k10, k5, k1 = 0, 0, 0
n, y = map(int, input().split())
for l in range((y // 10000) + 1):
    if y - l * 10000 > (n - l) * 5000:
        continue
    for m in range(((y - l * 10000) // 5000) + 1):
        if 5000 * m + (n - l - m) * 1000 == y - l * 10000:
            k10, k5, k1 = l, m, (n - l - m)
            break
    else:
        continue
    break
if [k10, k5, k1] == [0, 0, 0]:
    print('-1 -1 -1')
else:
    print(k10, end=' ')
    print(k5, end=' ')
    print(k1)
