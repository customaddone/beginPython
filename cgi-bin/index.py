# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
"""
5
1 5 7 10 21
4
2 4 17 8
"""
n = int(input())
a = list(map(int, input().split()))
q = int(input())
listans = list(map(int, input().split()))
"""
#解法１　dp部分和
def part_sum(a, A):
    N = len(a)
    dp = [[0] * (A + 1) for i in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A + 1):
            if a[i] <= j:
                dp[i + 1][j] = dp[i][j - a[i]] + dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[N][A]

for i in listans:
    print('yes' if part_sum(a, i) else 'no')
"""
"""
#解法２　再帰
def dfs(i, sum, ans):
    if i == len(a):
        return sum == ans
    if sum > ans:
        res = dfs(i + 1, sum, ans)
    else:
        res = dfs(i + 1, sum, ans) + dfs(i + 1, sum + a[i], ans)
    dp[i][sum] = res
    return dp[i][sum]

for i in listans:
    dp = [[0] * sum(a) for _ in range(n)]
    print('yes' if dfs(0, 0, i) else 'no')
"""
"""
#解法３　bit全探索
def bitsum(ans):
    flag = False
    for bit in range(1 << n):
        sum = 0
        for u in range(n):
            if bit & (1 << u):
                sum += a[u]
        if sum == ans:
            flag = True
    return flag
for i in listans:
    print('yes' if bitsum(i) else 'no')
"""
