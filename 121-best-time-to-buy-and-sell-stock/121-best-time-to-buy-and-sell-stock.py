class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0        
        buy = profit = 0
        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            if buy < sell:
                profit = max(profit, prices[sell]-prices[buy])
        return profit
