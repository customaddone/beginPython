n = 6
a =  [3,7,8,12,13,18]
A = 27
def rec_memo(i, sum):
    if sum < A and dp[i][sum]:
        return dp[i][sum]
    if i == n:
        return sum == A
    if sum > A:
        return False
    else:
        res = (rec_memo(i + 1, sum) or rec_memo(i + 1, sum + a[i]))
        if sum < A:
            dp[i][sum] = res
        return res
dp = [[0] * (A + 1) for i in range(n + 1)]
print(rec_memo(0, 0))
