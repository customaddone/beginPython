# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja
n, m = map(int, input().split())
coin = list(map(int, input().split()))
dp = [float('inf') for i in range(n + 1)]
dp[0] = 0

# n <= 50000なのでfor文ループさせるのはやめてほしい
def rec_memo(j):
    if dp[j] <= 50000:
        return dp[j]
    res = float('inf')
    for r in range(m):
        if coin[r] <= j:
            res = min(res, rec_memo(j - coin[r]) + 1)
    dp[j] = res
    return res
print(rec_memo(n))
