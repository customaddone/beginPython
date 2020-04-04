# これだとTLE
n, q = map(int, input().split())
s = input()
for i in range(q):
    l,r = map(int, input().split())
    ans = 0
    for j in range(l - 1, r - 1):
        if s[j] == "A" and s[j + 1] == "C":
            ans += 1
    print(ans)
