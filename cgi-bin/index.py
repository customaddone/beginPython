# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b
n = int(input())
AB = []
# setは超早いので使おう
# 中央の点が一番速いらしい
S = set()
for _ in range(n):
    a, b = map(int, input().split())
    AB.append((a, b))
    S.add(a)
    S.add(b)
def cost(u,v,a,b):
    tmp1=abs(u-a)+abs(a-b)+abs(v-b)
    tmp2=abs(u-b)+abs(a-b)+abs(v-a)
    return min(tmp1,tmp2)

ans=float('inf')
for u in S:
    for v in S:
        tmp=0
        for a,b in AB:
            tmp+=cost(u,v,a,b)
        ans=min(ans,tmp)
print(ans)
print(S)
"""
n = int(input())
lista = []
listb = []
ans = float('inf')

for i in range(n):
    a, b = map(int, input().split())
    lista.append([a, b])
    listb.append(a)
    listb.append(b)
listb.sort()
for i in range(len(listb)):
    for j in range(i, len(listb)):
        sum = 0
        for k in range(n):
            sum += abs(lista[k][0] - listb[i]) + (lista[k][1] - lista[k][0]) + abs(lista[k][1] - listb[j])
        ans = min(ans, sum)
print(ans)
"""
