n, m, c = map(int, input().split())
b = list(map(int, input().split()))
counter = 0
for i in range(n):
    a = list(map(int, input().split()))
    counter += ((sum([x * y for x, y in zip(a, b)]) + c) > 0)
print(counter)
