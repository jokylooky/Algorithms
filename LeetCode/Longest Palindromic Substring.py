'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxx = s[0]

        def fromCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(0, len(s)):
            first = fromCenter(i, i)
            second = fromCenter(i, i + 1)

            if len(first) > len(maxx):
                maxx = first
            if len(second) > len(maxx):
                maxx = second

        return maxx

sc = Solution()
print(sc.longestPalindrome("tattarrattat"))
print(sc.longestPalindrome("aa"))