s = input()
n = len(s)

ans = 0

for bit in range(1 << n):
    f = s[0]
    for i in range(n):
        if bit & (1 << n):
            f + "+"
        f += s[i + 1]
    ans += sum(map(int, f.split("+")))
print(ans)
