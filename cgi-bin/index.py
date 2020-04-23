# https://atcoder.jp/contests/abc114/tasks/abc114_c?lang=ja
n = int(input())

ans = 0

def dfs(s):
    global ans
    # 最初はdfsするのみ
    if s:
        # int型でn超えてるか判定
        if int(s) > n:
            return
        elif "3" in s and "5" in s and "7" in s:
            ans += 1
    dfs(s + "3")
    dfs(s + "5")
    dfs(s + "7")
dfs("")
print(ans)
