# n,n-1,n-2と小さく再帰し1以下になったら止まる
# fib(n)の数をメモっておくと楽になる
memo = [0] * 100

def fib(n):
    if n <= 1:
        return n;
    if (memo[n] != 0):
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
print(fib(40))
