from copy import deepcopy

def dfs(now, ignore, sumtime):
    global ans
    # (i<<n) - 1 全ての場所を訪れる
    if ignore == (1<<n) - 1:
        ans = min(ans, sumtime)
    dp[ignore][now] = sumtime
    print(dp[ignore][now])
    for i in dist[now]:
        # i[0]の位置が1
        if ignore>>i[0]&1 == 1:
            continue
        # ignore.append(i[0])
        nignore = ignore|1<<i[0]
        dfs(i[0], nignore, sumtime + i[1])

n = 4
ans = 1000000
dp = [[-1] * n for i in range(1<<n)]
dist = [
        [[1, 8], [2, 7], [3, 3]],
        [[0, 8], [2, 9]],
        [[0, 7], [1, 9], [3, 4]],
        [[0, 3], [2, 4]]
       ]

dfs(0, 1, 0)
print(ans)
