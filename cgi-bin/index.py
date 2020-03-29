ans = 0

def dfs(1, a, b):
    if i == n:
        ans = min(ans, max(a, b))
    else:
        dfs(i + 1, a + t[i], b)
        dfs(i + 1, a, b + t[i])

n = int(input())
t = [int(input()) for i in range(n)]

dfs(0, 0, 0)
print(ans)
