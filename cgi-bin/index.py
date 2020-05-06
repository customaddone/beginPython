N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
# 貪欲法
# 筐体に勝つ手を出したかどうか
# 勝たない手を出せないこともある
flag = [0] * N
ans = 0
for i in range(N):
    # K回目以降 and 今回勝てる手がK回前の勝てる手と一致している and K回前に実際に勝てる手を出した
    # K回前に出して今回出さないのも、K回前に出さずに今回出すのも同じ特典になる
    if i - K >= 0 and T[i - K] == T[i] and flag[i - K]:
        continue
    if T[i] == 'r':
        ans += P
    elif T[i] == 's':
        ans += R
    else:
        ans += S
    flag[i] = True
print(ans)

# K = 3なら1番目, 4番目, 7番目...のものを抽出してdp
# 影響のあるものだけを抽出する
def calc(l):
    n = len(l)
    dp = [[0]*3 for _ in range(n+1)]

    for i in range(n):
        if l[i]=='r':
            dp[i+1][0] = max(dp[i][1], dp[i][2])
            dp[i+1][1] = max(dp[i][0], dp[i][2])
            dp[i+1][2] = max(dp[i][0], dp[i][1])+P
        elif l[i]=='s':
            dp[i+1][0] = max(dp[i][1], dp[i][2])+R
            dp[i+1][1] = max(dp[i][0], dp[i][2])
            dp[i+1][2] = max(dp[i][0], dp[i][1])
        else:
            dp[i+1][0] = max(dp[i][1], dp[i][2])
            dp[i+1][1] = max(dp[i][0], dp[i][2])+S
            dp[i+1][2] = max(dp[i][0], dp[i][1])

    return max(dp[n])

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
ans = 0

for i in range(K):
    l = []
    j = i

    # K個飛ばしでlに入れる
    for j in range(i, N, K):
        l.append(T[j])

    # Tの[K = 3なら1番目, 4番目, 7番目...]でcalc
    ans += calc(l)

print(ans)
