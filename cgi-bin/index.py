a, b, c, x, y = map(int, input().split())
ans = x*a+y*b
for i in range(max(x, y) + 1):
    p = c * i * 2 + max(0, x - i) * a + max(0, y - i) * b
    ans = min(ans, p)
print(ans)
