n, a, b = map(int, input().split())
ans = 0
for n in range(1, n + 1):
    if a <= sum([int(i) for i in list(str(n))]) <= b:
        ans += n
print(ans)
