n = 3
k = 6
a = [1, 2, 3, 4, 5]

# 2 ** n 通り試行がある
def dfs(i, sum):
    if i == n:
        print(sum)
        return sum == k

    # 掘り進んだ先にTrueがあるようなら
    if dfs(i + 1, sum):
        return True

    if dfs(i + 1, sum + a[i]):
        return True

    return False

print(dfs(0, 0))
