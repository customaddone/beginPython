d, n = map(int, input().split())
t = [int(input()) for i in range(d)]
lista = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for i in range(n)] for i in range(d)]
# 本日の服で一つ、前日の服で一つループさせる
# 日にち
for i in range(1, d):
    # 今日着る服
    for j in range(n):
        # 昨日着てた服
        for k in range(n):
            # もし今日選ぶ服が温度に適合していて           昨日着てた服が昨日の気温に適合していた時
            if lista[j][0] <= t[i] <= lista[j][1] and lista[k][0] <= t[i - 1] <= lista[k][1]:
                # dpはkを回した時にできた他のdp[i][j] vs 今日着た服の派手さと前日に着た服の派手さの差 + 前日のdp
                dp[i][j] = max(dp[i][j], abs(lista[j][2] - lista[k][2]) + dp[i - 1][k])
# dpの最後尾をprint
print(max(dp[-1]))
