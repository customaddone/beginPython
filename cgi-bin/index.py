ans = []
a = [(2, 3),(1, 2),(3, 4),(2, 2)]
n = 4
w = 5

def dfs(i, weight, sum):
    if i == n:
        if weight <= w:
            ans.append(sum)
        return sum

    return dfs(i + 1, weight, sum) + dfs(i + 1, weight + a[i][0], sum + a[i][1])
# dfsは初っ端で呼ばれてしまうらしい（ansの宣言より前)
dfs(0, 0, 0)
print(max(ans))
