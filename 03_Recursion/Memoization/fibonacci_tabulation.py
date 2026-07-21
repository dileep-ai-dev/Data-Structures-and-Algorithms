def fibonacci(n):
    dp = [-1] * (n + 1)

    for i in range(n + 1):
        if i == 0 or i == 1:
            dp[i] = i
        else:
            dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fibonacci(6))