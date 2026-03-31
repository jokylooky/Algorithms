# Minimum Size Subarray Sum

def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    curr_sum = 0
    best = float('inf')

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            best = min(best, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    return best if best != float('inf') else 0

print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))