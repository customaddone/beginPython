N = int(input())
# 結合
s = ["".join(sorted(input())) for i in range(N)]
# dict使ってハッシュ使っていい感じにカウントできる
D = dict()
for st in s:
    if st in D:
        D[st] += 1
    else:
        D[st] = 1
ans=0
for i in D:
    k = D[i]
    ans += (k * (k-1)) // 2
print(ans)
