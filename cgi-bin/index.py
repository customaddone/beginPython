memo = {1: 1, 2: 1}
def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    # 9: 34 みたいにメモられる
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

fibonacci(10)
print(memo)
