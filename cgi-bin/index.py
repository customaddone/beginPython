#「P内」のPの最大値のインデックス
n = int(input())
S = []
P = []
name = 'atcoder'
for i in range(n):
    s, p = input().split()
    S.append(s)
    P.append(int(p))
if max(P)>(sum(P)/2):name=S[P.index(max(P))]
print(name)
