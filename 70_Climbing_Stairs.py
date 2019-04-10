class Solution:
    def climbStairs(self, n: int) -> int:
        d = [0] * n

        if n == 1:
            return 1
        elif n == 2:
            return 2

        d[0] = 1
        d[1] = 2

        for i in range(2, n):
            d[i] = d[i - 1] + d[i - 2]

        return d[n - 1]