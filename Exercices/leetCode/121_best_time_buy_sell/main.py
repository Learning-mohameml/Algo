from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # ============== Brut force : O(n^2) =================
        # n = len(prices)
        # max_profit = 0 

        # for i in range(n - 1) : 
        #     prices_next = [prices[j] for j in range(i+1 , n)]
        #     max_price_next = max(prices_next)

        #     if max_price_next > prices[i] : 
        #         max_profit  = max(max_profit , max_price_next - prices[i])

        # return max_profit
    
        # ============== Slinding Window : O(n) ===================

        if len(prices) == 1 : 
            return 0 


        left = 0 
        right = 1 
        profit = 0 

        while right < len(prices) : 
            new_profit = prices[right] - prices[left]
            profit = max(profit , new_profit)

            if new_profit < 0 : 
                left = right
            right += 1 

        return profit 



# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
prices = [2,1,2,1,0,1,2] # 2 



max_porofit = Solution().maxProfit(prices)

print(max_porofit)