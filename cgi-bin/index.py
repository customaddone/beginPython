# breakで抜けなかったときのみelseが実行される
n, m, a, b = map(int, input().split())
ans = 'complete'
for i in range(m):
    if n <= a:
        n += b
    n -= int(input())
    if n < 0:
        print(i + 1)
        break
else:
    print("complete")
