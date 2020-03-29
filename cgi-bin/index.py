a = [1,2,3,4,5]
def dfs(i, value):
    if i == n - 1:
        print(value)
        if value % 2 == 0:
            return value
        else:
            return 0
    return dfs(i + 1, value * a[i + 1]) + dfs(i + 1, value)

n = int(input())
print(dfs(0, a[0]))
