# ttp://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja
n = int(input())
dp = [0] * (n + 1)
def fibonatti(n):
    if dp[n] > 0:
        return dp[n]
    if (n == 0) or (n == 1):
        return 1
    else:
        dp[n] = fibonatti(n - 1) + fibonatti(n - 2)
        return dp[n]
print(fibonatti(n))
