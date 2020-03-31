coin = [1, 5, 10, 50, 100, 500]

chave = list(map(int, input().split()))
a = int(input())
ans = 0


for i in range(6):
    pay = min(a // coin[5 - i], chave[5 - i])
    a = a - coin[5 - i] * pay
    ans += pay
print(ans)
