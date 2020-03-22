#　割る9の取り分、割る6の取り分をi, N - iで決めて1 <= i <= N + 1の範囲で動かす
N = int(input())
ans = N
# 0, 1, 2, 3... 127
for i in range(N + 1):
    cnt = 0
    # t = 1
    t = i
    while t > 0:
        # tを6で割った余りをcntに足す
        cnt += t % 6
        # tを６で割ったときの商を求める→余りを足す...
        t //= 6
    j = N - i
    while j>0:
        cnt+=j%9
        j//=9
    ans = min(ans,cnt)
print(ans)
