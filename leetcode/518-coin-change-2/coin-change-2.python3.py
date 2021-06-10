class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]

# dp := make([]int, amount+1)
#     dp[0] = 1
#     for _, coin := range coins {
#         for i := coin; i <= amount; i++ {
#             dp[i] += dp[i-coin]
#         }
#     }
#     return dp[amount]
