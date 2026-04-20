'''
3761. Minimum Absolute Distance Between Mirror Pairs

You are given an integer array nums.
A mirror pair is a pair of indices (i, j) such that:

0 <= i < j < nums.length, and
reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed by reversing the digits of x.
Leading zeros are omitted after reversing, for example reverse(120) = 21.

Return the minimum absolute distance between the indices of any mirror pair.
absolute distance between indices i and j is abs(i - j).

If no mirror pair exists, return -1.

Input: nums = [12,21,45,33,54]
Output: 1
Explanation:
The mirror pairs are:

(0, 1) since reverse(nums[0]) = reverse(12) = 21 = nums[1], giving an absolute distance abs(0 - 1) = 1.
(2, 4) since reverse(nums[2]) = reverse(45) = 54 = nums[4], giving an absolute distance abs(2 - 4) = 2.
The minimum absolute distance among all pairs is 1.
'''


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        minlen = len(nums)
        hash_dict = {}
        for i in range(len(nums)):
            if nums[i] in hash_dict:
                minlen = min(minlen, abs(hash_dict[nums[i]] - i))
                if minlen == 1:
                    return 1
            hash_dict[int(str(nums[i])[::-1])] = i

        return -1 if minlen == len(nums) else minlen


sc = Solution()
print(sc.minMirrorPairDistance([12,21,45,33,54]))
print(sc.minMirrorPairDistance([21,120]))
print(sc.minMirrorPairDistance([120,21]))