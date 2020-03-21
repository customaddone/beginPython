n, m, c = map(int, input().split())
*b, = map(int, input().split())
counter = 0
for i in range(n):
    *a, = map(int, input().split())
    value = sum([a * b for a, b in zip(a,b)]) + c
    counter += (value > 0)
print(counter)
