# https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_b
import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
a = [int(input()) for i in range(n)]
dp = [[-1] * n for i in range(n)]

def f(l, r, s):
    if dp[l][r] >= 0:
        pass
    elif l == r:
        if s:
            dp[l][r] = 0
        else:
            dp[l][r] = a[l]
    elif s:
        if a[l] > a[r]: dp[l][r] = f((l + 1) % n, r, 0)
        else: dp[l][r] = f(l,(r-1) % n, 0)
    else:
        dp[l][r] = max(f((l+1) % n, r, 1) + a[l],f(l,(r - 1) % n, 1) + a[r])
    return dp[l][r]

ans = 0
for i in range(n):
    ans = max(ans,f((i + 1) % n,(i + n - 1) % n, 1) + a[i])
print(ans)
