n, m = map(int, input().split())
s, c = [], []
for m in range(M):
    s,c=map(int,input().split())
    S.append(s)
    C.append(c)
# n = 3なら1000まで
for i in range(10 ** n):
    # 10**n以下の数字を全て並べて条件に適合するやつだけ抽出
    if len(str(i)) == N and all(str(i)[s - 1] == str(c) for s, c in zip(s, c)):
        print(i)
        break
else:
    print(-1)
