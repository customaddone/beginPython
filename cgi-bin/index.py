# https://www.ioi-jp.org/joi/2007/2008-ho-prob_and_sol/2008-ho.pdf#page=6
# 022.5 重複ありナップサック問題
n, m = map(int, input().split())
p = [int(input()) for i in range(n)]

def rec_memo(i, j):
    if dp[i][j] >= 0:
        return dp[i][j]
    if i == n:
        return 0
    else:
        res = rec_memo(i + 1, j)
        for r in range(n):
            if j > p[r]:
                res = max(res, rec_memo(i + 1, j - p[r]) + p[r])
    dp[i][j] = res
    return res

dp = [[-1] * (m + 1) for i in range(n + 1)]
print(rec_memo(0, m))
