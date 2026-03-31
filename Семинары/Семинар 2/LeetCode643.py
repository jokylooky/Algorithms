def find_max_avg(nums: list[int], k:int) -> float:
    window = sum(nums[:k])
    best = window

    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)

    return best / k

print(find_max_avg([1, 2, 3, 4, 5], 3))