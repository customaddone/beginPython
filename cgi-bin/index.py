# n,n-1,n-2と小さく再帰し1以下になったら止まる
def fib(n):
    if n <= 1:
        return n;
    return fib(n - 1) + fib(n - 2)

print(fib(8))
