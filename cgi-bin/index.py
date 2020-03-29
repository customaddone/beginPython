def dfs(i, f):
    if i == n - 1:
        return sum(list(map(int, f.split("+"))))

    # 末端まで行くと数字をリターンする
    # 2つ合わせたもの、４つ合わせたもの...が帰ってくる
    return dfs(i + 1, f + s[i + 1]) + dfs(i + 1, f + "+" + s[i + 1])

s = input()
n = len(s)

print(dfs(0, s[0]))
