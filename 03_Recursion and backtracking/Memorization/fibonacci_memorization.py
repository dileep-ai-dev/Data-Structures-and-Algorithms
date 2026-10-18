def fibonacci(n, dp=None):
    if dp is None:
        dp = [-1] * (n + 1)

    if n == 0:
        return 0

    if n == 1:
        return 1

    if dp[n] == -1:
        dp[n] = fibonacci(n - 1, dp) + fibonacci(n - 2, dp)

    return dp[n]


print(fibonacci(6))