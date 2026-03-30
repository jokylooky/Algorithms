'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''

def two_Sum(nums, target):
    hash_dict = {} # создаю хэш-табличку (словарь в питоне)

    for i in range(len(nums)):
        diff = target - nums[i] # считаю разницу искомого и i-го числа и записываю её в словарь, как ключ. значение - индекс
        if diff in hash_dict:
            return [hash_dict[diff], i] # если разница есть в словаре, возвращаю её ключ (индекс) и текущий индекс
        hash_dict[nums[i]] = i # в любом случае, добавляю в словарь само число и его индекс

    return None

print(two_Sum([2,7,11,15], 9))