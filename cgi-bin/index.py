n = int(input())

ans = 0

def dfs(s):
    global ans
    if s:
        if int(s) > n:
            return
        elif "3" in s and "5" in s and "7" in s:
            ans += 1
    dfs(s + "3")
    dfs(s + "5")
    dfs(s + "7")
dfs("")
print(ans)
