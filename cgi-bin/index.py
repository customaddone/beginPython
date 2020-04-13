a,b,x = map(int,input().split())
mi = 0
ma = 10**9+1
# 上限と下限を徐々に狭めていく
# 上限-下限＝１になったら下限が答え
while ma-mi>1:
  me = int((mi+ma)/2)
  if a*me+b*len(str(me))<=x:
    mi = me
  else:
    ma = me
print(mi)
