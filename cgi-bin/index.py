n,a,b=map(int,input().split())
m=10**9+7

# 強化版cmb
def cmb(x,y):
    r=1
    for i in range(1,y+1):
        # 5C3なら
        # 5 * 4 * 3 / 3 * 2 * 1
        # = 5(mod m) * 1 / 3(mod m) * 4 (mod m) * 1 / 2(mod m) * 3(mod m) * 1 / 1(mod m)
        # (x- i + 1): 5 - 1 + 1...
        # pow(i,m-2,m):
        # フェルマーの小定理 a ** (m - 2) (mod m) = 1 / a (mod d)
        # 1 / a (mod m) はaで掛けると1 (mod m)になる数
        # 1 / 2なら500000004
        r=(r*(x-i+1)*pow(i,m-2,m))%m
    return r
# powでmod累乗を楽にできる
print((pow(2,n,m)-1-cmb(n,a)-cmb(n,b))%m)
