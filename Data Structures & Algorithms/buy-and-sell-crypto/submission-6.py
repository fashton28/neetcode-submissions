class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #let's think through this problem without any specific algorithm in mind.
        #given an array
        #find maximum profit
        #buy at lowest price and sell at highest price.
        #implement a dynamic sliding window. or a double for loop, which wouldn't be efficient at all.

        lowest = prices[0]
        profit = 0


        #[7,6,4,3,1]
        for i in range(1,len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            elif prices[i] - lowest > profit:
                profit = prices[i] - lowest

        return profit

