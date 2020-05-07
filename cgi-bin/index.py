n = int(input())
ng1 = int(input())
ng2 = int(input())
ng3 = int(input())

# ある条件下で数を足し上げられるかはdpが使える
dp = [float('inf') for _ in range(301)]
dp[0] = 0
for i in range(len(dp)):
    if i in not [ng1, ng2, ng3]:
        # i - 3, i - 2, i - 1について調べる
        for j in range(max(i - 3), i):
            dp[i] = min(dp[i], dp[j] + 1)
print('YES' if 0 <= dp[n] <= 100 else 'NO')
