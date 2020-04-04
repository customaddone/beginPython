n, q = map(int, input().split())
s = input()
ls = [0]
# 判定のたびにいちいち配列にアクセスしていては時間がかかる
for i in range(n - 1):
    # 累積値をappendしていく
    if s[i] == "A" and s[i + 1] == "C":
        ls.append(ls[i] + 1)
    else:
        ls.append(ls[i])

for i in range(q):
    l,r = map(int, input().split())
    print(ls[r - 1] - ls[l - 1])
