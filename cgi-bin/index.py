a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# メモ用意してスッキリ
def rec(i):
    if dp[i]:
        return dp[i]
    if i == n:
        res = 0
    else:
        res = max(rec(i + 1), rec(i + 1)+ a[i])
    dp[i] = res
    return res

n = 20
dp = [0] * (n + 1)
print(rec(0))
