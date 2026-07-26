class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] = number of ways to make amount i
        dp = [0] * (amount + 1)
        dp[0] = 1   # base case: one way to make 0 (choose nothing)

        # iterate coins first to avoid counting permutations
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]

        