n = int(input())
s = input()

def alter(str):
    if str == 'J':
        return 0
    elif str == 'O':
        return 1
    elif str == 'I':
        return 2
# i日目にJ(001),O(010),I(100),JO(110)...が参加する通りが何通りあるかdpしておく
dp = [[0] * ((1 << 3)) for i in range(n + 1)]
# 0日目はJが参加した
s = ["J"] + list(s)
dp[0][1 << 0] = 1
# 施行回数
for i in range(1, n + 1):
    # i日目の責任者を含む組み合わせ
    for u in range(1 << 3):
        if u & (1 << alter(s[i])):
            # i日目u, i - 1日目kの通りを求める
            for k in range(1 << 3):
                if u & k:
                    dp[i][u] += dp[i - 1][k]
                    # これprintする時にもやらないと意味ないよ
                    # 忘れないで
                    # 忘れないで
                    dp[i][u] %= 10007
print(sum(dp[-1]) % 10007)
