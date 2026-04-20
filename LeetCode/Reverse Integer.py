'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321
'''


class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        newValue = 0

        while x != 0:
                newValue = newValue * 10 + x % 10
                x = x // 10

        if -2147483648 <= newValue <= 2147483648 - 1:
            return -newValue if negative else newValue
        else:
            return 0


sc = Solution()
print(sc.reverse(1))
print(sc.reverse(-123))
print(sc.reverse(1534236469))