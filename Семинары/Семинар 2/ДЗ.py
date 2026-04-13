'''
Вариант 3
'''

'''
Задача 3.1. Дан массив целых чисел nums и число k. Определить, существуют ли в массиве два одинаковых элемента, 
расстояние между индексами которых не превышает k.

Вход:  nums = [1, 2, 3, 1], k = 3
Выход: True

Вход:  nums = [1, 2, 3, 1, 2, 3], k = 2
Выход: False
'''
print(f"{"ВАРИАНТ 3":=^21}\n")

def fixed_window_len(nums, k):
    if len(nums) < k:
        return None

    for i in range(k, len(nums)):
        if nums[i] == nums[i - k]:
            return True

    return False

print('Задача 1.1 -', fixed_window_len([1, 2, 3, 1], 3))
print('Другие данные -', fixed_window_len([1, 2, 3, 1, 2, 3], 2), '\n')

'''
Задача 3.2. Дан бинарный массив nums (содержит только 0 и 1) и число k. Можно заменить не более k нулей на единицы. 
Найти длину наибольшего непрерывного подмассива, состоящего из единиц.

Вход:  nums = [1, 1, 0, 0, 1, 1, 1, 0, 1], k = 2
Выход: 8
Пояснение: заменяем нули на позициях 2 и 7
'''

def longest_one(nums, k):
    left = 0
    zeros = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print('Задача 2.', longest_one([1, 1, 0, 0, 1, 1, 1, 0, 1], 2), '\n')

'''
Задача 3.3. Дан массив целых чисел nums. Найти все уникальные тройки элементов, сумма которых равна нулю. 
Тройки не должны повторяться.

Вход:  nums = [-1, 0, 1, 2, -1, -4]
Выход: [[-1, -1, 2], [-1, 0, 1]]
'''

def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            summa = nums[i] + nums[left] + nums[right]
            if summa == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif summa < 0:
                left += 1
            else:
                right -= 1

    return result

print('Задача 3.', three_sum([-1, 0, 1, 2, -1, -4]))