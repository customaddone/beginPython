n = int(input())
dp = [1]*(n + 1)
ans = 0
# エラストテネスの箒
for i in range(2, n + 1):
    div = 1
    while i * div <= n:
        dp[i * div] += 1
        div += 1
# dp[1]から１個飛ばしで表示
print(dp[1::2])
