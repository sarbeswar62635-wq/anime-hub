import ast
class Solution:
    def maxprofit(self,prices):
        min_price = float('inf')
        max_profit =  0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price-min_price > max_profit:
                max_profit = price-min_price
        return max_profit
num = ast.literal_eval(input(" enter the price as form of list "))
Profit = Solution()
print(Profit.maxprofit(num))