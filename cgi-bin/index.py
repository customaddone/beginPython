# O(n3)程度であれば十分間に合う
n = int(input())
a = list(map(int, input().split()))
ans = 0
for l in range(n):
    for m in range(l + 1, n):
        for q in range(m + 1, n):
            if a[l] + a[m] > a[q]:
                ans = max(ans, a[l] + a[m] + a[q])
print(ans)
