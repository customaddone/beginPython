# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1167&lang=jp
# 個数制限なし重複ありナップサックdp
def tetrafunc(n, list):
    l = len(list)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n + 1):
        for j in range(l):
            if i >= list[j]:
                dp[i] = min(dp[i], dp[i - list[j]] + 1)
    return dp[n]

# n以下の正四面体数をリストアップ
def tetraall(n):
    listtetra = []
    tetraint = 0
    i = 1
    while n > tetraint:
        tetraint = i * (i + 1) * (i + 2) // 6
        listtetra.append(tetraint)
        i += 1
    return listtetra

# n以下の奇数の正四面体数をリストアップ
def tetraodd(n):
    listtetra = []
    tetraint = 0
    i = 1
    while n > tetraint:
        tetraint = i * (i + 1) * (i + 2) // 6
        if tetraint % 2 != 0:
            listtetra.append(tetraint)
        i += 1
    return listtetra

n = int(input())
print(tetrafunc(n, tetraall(n)), end = " ")
print(tetrafunc(n, tetraodd(n)))
