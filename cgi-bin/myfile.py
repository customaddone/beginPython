
n, k = map(int, input().split())
sum = 0
for i in range(k, n + 2):
    sum += n * i - (i ** 2) + i + 1
print(sum // 10 ** 9 + 7)
