# Find All Anagrams in Code

from collections import Counter

def find_anagrams(s: str, p: str) -> list[int]:
    k = len(p)
    if k > len(s):
        return []

    p_count = Counter(p)
    s_count = Counter(s[:k])
    result = []

    if s_count == p_count:
        result.append(0)

    for i in range(k, len(s)):
        # Добавляем правый символ
        s_count[s[i]] += 1
        # Убираем левый символ
        left = s[i - k]
        s_count[left] -= 1
        if s_count[left] == 0:
            del s_count[left]
        if s_count == p_count:
            result.append(i - k + 1)

    return result

print(find_anagrams("cbaebabacd", "abc"))