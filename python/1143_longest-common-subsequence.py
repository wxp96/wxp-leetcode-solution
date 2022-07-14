class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(m):
            dp1 = [0] * (n + 1)
            for j in range(n):
                if text1[i] == text2[j]:
                    dp1[j + 1] = dp[j] + 1
                else:
                    dp1[j + 1] = max(dp1[j], dp[j + 1])
            dp = dp1
        return dp[n]