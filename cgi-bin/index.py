# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_d
n = int(input())
s = [list(input()) for i in range(5)]

dp = [[5, 5, 5] for i in range(n)]

# dpの初期設定が重要
for i in range(5):
    for j in range(n):
        # その色が出現した都度1を引く
        if s[i][j] == "R":
            dp[j][0] -= 1
        elif s[i][j] == "B":
            dp[j][1] -= 1
        elif s[i][j] == "W":
            dp[j][2] -= 1

# print(dp)
# [4, 4, 4],
# [4, 4, 3],
# [3, 4, 4]

# iが列、jが色
for i in range(1, n):
    for j in range(3):
        # j以外の色で前の列を塗った時の最小値
        dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j - 2])
print(min(dp[-1]))
