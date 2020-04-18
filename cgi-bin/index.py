memo = [0] * 100

def fibonatti(n):
    if memo[n] > 0:
        return memo[n]
    if (n == 1) or (n == 2):
        return 1
    memo[n] = fibonatti(n - 1) + fibonatti(n - 2)
    return memo[n]

print(fibonatti(40))
