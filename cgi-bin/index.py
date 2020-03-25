s = list(input())
t = input()
ans = 'No'
for _ in range(len(s)):
    s.insert(0, s.pop())
    if ''.join(s) == t:
        ans = 'Yes'
print(ans)

# 模範解答
# 文字列を二つ繋げてその中に目的の文字列があるか
print("Yes" if input() in input()*2 else "No")
