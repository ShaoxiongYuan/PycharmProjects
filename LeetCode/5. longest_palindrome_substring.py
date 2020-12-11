# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''
        if len(s) == 1:
            return s

        for i in range(len(s)):
            for j in range(len(s) + 1):
                if len(m) >= j - i:
                    continue
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    continue

        return m


s = Solution()
print(s.longestPalindrome('ababcd'))
