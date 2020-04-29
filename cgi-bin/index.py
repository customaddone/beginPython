#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=ja
n = int(input())
dist = [[] for i in range(n)]
dp = [[0, 0] for i in range(n)]

for i in range(n):
    d = list(map(int, input().split()))
    if len(d) > 2:
        # 2文字目以降をappend
        for j in d[2:]:
            dist[i].append(j - 1)
cnt = 0
def dfs(pos):
    global cnt
    # 初めての訪問なら
    if dp[pos][0] == 0:
        cnt += 1
        dp[pos][0] = cnt
    for i in dist[pos]:
        dfs(i)
    # for回し終えてこれが最後の訪問なら
    if dp[pos][1] == 0:
        cnt += 1
        dp[pos][1] = cnt
dfs(0)
for i in range(n):
    print(i + 1, end = " ")
    print(dp[i][0], end = " ")
    print(dp[i][1])
