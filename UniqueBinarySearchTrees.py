class Solution: # time complexity O(n)
    def numTrees(self, n: int) -> int:  # bottom-up DP approach (tabulation)
        if n == 0 or n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            # calculate number of unique binary trees for size i , dp[j] represents left subtree possibilities,
            # while dp[i - j - 1] is for the right subtree possibilities
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]

    """
    def numTrees(self, n: int) -> int: 
    # runtime complexity : Exponential O(2^n)  #! TimeLimit Exceeded
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2

        total = 0
        for i in range(n):
            left = self.numTrees(i)
            right = self.numTrees(n - i - 1)
            total += left * right

        return total
    """
