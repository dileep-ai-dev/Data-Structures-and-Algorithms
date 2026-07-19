# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1 / x
            n = -n

        base = x
        exp = n
        result = 1

        while exp > 0:
            if exp % 2 == 1:
                result *= base

            base *= base
            exp //= 2
        return result
