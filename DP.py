class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num = [1E4+1]*(amount+1) # from $0 to $amount
        num[0] = 0 # $0 can be made up by 0 coins
        
        for value in range(1, amount+1):
            for coin in coins:
                preValue = value - coin
                if (preValue < 0):
                    continue
                
                num[value] = min(num[value], num[preValue]+1)
        
        if num[amount] > 1E4:
            return -1
        else:
            return num[amount]
        