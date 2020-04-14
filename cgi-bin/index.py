def part_sum(a,A):
    p=10**9+7
    #初期化
    N=len(a)
    dp=[[0 for i in range(A+1)] for j in range(N+1)]
    # i番目までの整数からいくつか選んで総和をjにすることができるか
    # 0番目までの整数からいくつか選んで総和を0にすることができるか
    dp[0][0]=1

    #DP
    for i in range(N):
        for j in range(A+1):
            # dp[i][j−a[i]]がTrueなら、dp[i+1][j]もTrue（足せばいいので）
            if a[i]<=j: #i+1番目の数字a[i]を足せるかも
                dp[i+1][j]=dp[i][j-a[i]]+ dp[i][j]% p
            else: #入る可能性はない
                dp[i+1][j]=dp[i][j]%p
    return dp[N][A]

a = [1, 3, 5, 7, 9]
A = 10
print(part_sum(a, A))
