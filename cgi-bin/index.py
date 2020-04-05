def dfs(i, f, sum):
    if i == 3:
        if sum == 7:
            print(f + "=7")
            exit()

    else:
        dfs(i + 1, f + "-" + s[i + 1], sum - int(s[i + 1]))
        dfs(i + 1, f + "+" + s[i + 1], sum + int(s[i + 1]))

s = input()

dfs(0, s[s], int(s[0]))
