'''
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
'''

# метод двух указателей
def lengthOfLongestSubstring(s: str) -> int:
        n = len(s)
        used = {} # словарь для хранения символов и их индексов
        left, maxlen = 0, 0
        for right in range(n):
            if s[right] in used and used[s[right]] >= left:
                left = used[s[right]] + 1 # если символ повторяется и его индекс больше левого указателя, сдвигаем левый
            used[s[right]] = right
            maxlen = max(right - left + 1, maxlen)
        return maxlen

print(lengthOfLongestSubstring("abcabcbb"))