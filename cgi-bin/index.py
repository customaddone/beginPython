def LI(): return list(map(int,input().split()))
while True:
    n, x = LI()
    # AOJのお約束
    if n == x == 0:
        break
    ans = 0
    for i in range(1, n + 1):
        # 二段目はi + 1(i < j)からスタート
        for j in range(i + 1, n + 1):
            # 下記のようにすることでfor減らせる
            k = x - i - j
            # jより大きくnより小さい
            if j < k <= n:
                ans += 1
    print(ans)
