# print(*[])で配列内の文字全てをプリント
k, x = map(int, input().split())
print(*[x for x in range(x - k + 1, x + k - 1)])
