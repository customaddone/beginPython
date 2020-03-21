n, x = map(int, input().split())
donuts = [int(input()) for _ in range(n)]
print((x - sum(donuts)) // min(donuts) + len(donuts))
