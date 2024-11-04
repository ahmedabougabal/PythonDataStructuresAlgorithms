# class Solution:
#     # this approach got time limit exceeded whilst using cpp, it runs quite fine
#     def numTrees(self, n: int) -> int:
#         if n <= 1:
#             return 1
#         result = 0
#         for i in range(1, n+1):
#             result += self.numTrees(i-1) * self.numTrees(n-i)
#         return result
#

class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def helper(n):
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            total = 0
            for i in range(1, n + 1):
                total += helper(i-1) * helper(n - i)
                memo[n] = total
            return total

        return helper(n)
