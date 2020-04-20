n,a,b=map(int,input().split())
m=10**9+7

# 強化版cmb
def cmb(x,y):
    r=1
    for i in range(1,y+1):
        r=(r*(x-i+1)*pow(i,m-2,m))%m
    return r
# powでmod累乗を楽にできる
print((pow(2,n,m)-1-cmb(n,a)-cmb(n,b))%m)
