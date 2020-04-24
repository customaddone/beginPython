# https://atcoder.jp/contests/abc095/tasks/arc096_a
a, b, c, x, y = map(int, input().split())
n = max(x, y)
ans = float('inf')
# 別解 場合分けしてみる
# a + b < 2 * cなら
# ABピザを買わない
if a+b<2*c:
    print(x*a+y*b)
else:
    # aとbの共通部分についてABピザを賈う
    ans=2*c*min(x,y)
    if x>y:
        x=x-y
        # もしAピザ1枚よりABピザ2枚の方が安かったら
        if a<2*c:
            ans=ans+x*a
        else:
            ans=ans+x*2*c
    else:
        y=y-x
        if b<2*c:
            ans=ans+y*b
        else:
            ans=ans+y*2*c
    print(ans)
"""
# a + b < 2 * cなら
# ABピザ買わないみたいなこともできる
for i in range(n + 1):
    buyab = i * c * 2
    buya = max((x - i), 0) * a
    buyb = max((y - i), 0) * b
    sum = buyab + buya + buyb
    ans = min(ans, sum)
print(ans)
"""
