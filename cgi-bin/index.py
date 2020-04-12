import collections
m = int(input())
n = 1000000000
ans = []
listnum = [
            [0, 1],
            [0, 1, 2],
            [1, 2, 3],
            [2, 3, 4],
            [3, 4, 5],
            [4, 5, 6],
            [5, 6, 7],
            [6, 7, 8],
            [7, 8, 9],
            [8, 9]
           ]
def dfs(s):
    if len(str(n)) + 1 > len(s):
        ans.append(int(s))
        lastnum = str(s)[-1]
        for i in listnum[int(lastnum)]:
            dfs(s + str(i))
for i in range(1, 10):
    dfs(str(i))
ans = sorted(ans)
print(ans[m - 1])
