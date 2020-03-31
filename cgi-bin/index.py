from operator import itemgetter

n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

# key=itemgetter(1)で２番目の要素でソート
st = sorted([(s[i], t[i]) for i in range(n)], key=itemgetter(1))

ans = 0
last = 0

for i in range(n):
    if last < s[i][0]:
        ans += 1
        last = st[i][1]

print(ans)
