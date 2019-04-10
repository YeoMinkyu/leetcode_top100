import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        print(min_price)
        max_profit = 0

        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif (prices[i] - min_price) > max_profit:
                max_profit = prices[i] - min_price

        return max_profit