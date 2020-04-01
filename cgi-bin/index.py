def rec(i, j):
    if i == n:
        res = 0
        print([i, j, res])
    # オーバーフロー この先０になります
    elif j < w[i]:
        res = rec(i + 1, j)
    # v[i]の分だけ増えます
    else:
        res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i])

    return res

n = int(input())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

W = int(input())

print(rec(0, W))
