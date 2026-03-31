'''
Задача 1. Next Smaller Element

Для каждого элемента массива найти ближайший элемент правее, который строго меньше текущего. Если такого нет — -1.

Вход:  [4, 5, 2, 10, 8]
Выход: [2, 2, -1, 8, -1]
'''

def nextSmallerElement(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] >= nums[i]:
            stack.pop()

        if stack:
            res[i] = stack[-1]

        stack.append(nums[i])

    return res

print('Задача 1.', nextSmallerElement([4, 5, 2, 10, 8]))

'''
Задача 2. Удаление соседних дубликатов

Дана строка. Удалять пары соседних одинаковых символов, пока это возможно. Вернуть результат.

Вход:  "abbaca"
Выход: "ca"
Пояснение: "abbaca" → "aaca" → "ca"
'''

def removeDuplicates(s: str) -> str:
    stack = []

    for ch in s:
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
        stack.append(ch)

    return ''.join(stack)

print('Задача 2.', removeDuplicates("abbaca"))

'''
Задача 3. Валидация стековой последовательности

Даны два массива pushed и popped — последовательности push и pop операций. Определить, возможна ли такая последовательность.

pushed = [1, 2, 3, 4, 5]
popped = [5, 4, 3, 2, 1]  → True

pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]  → False

pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]  → False
'''

def validStackSeq(pushed: list[int], popped: list[int]) -> bool:
    return pushed == popped[::-1]

print('Задача 3:')
print('1) pushed = [1, 2, 3, 4, 5],  popped = [5, 4, 3, 2, 1] ->',validStackSeq([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
print('2) pushed = [1, 2, 3, 4, 5],  popped = [4, 5, 3, 2, 1] ->',validStackSeq([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print('3) pushed = [1, 2, 3, 4, 5],  popped = [4, 3, 5, 1, 2] ->',validStackSeq([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))

'''
Задача 4. Circular Next Greater Element

Тот же Next Greater Element, но массив циклический (после последнего элемента идёт первый).

Вход:  [1, 2, 1]
Выход: [2, -1, 2]  ← для последней 1 ответ — первая 2
'''
def circularNextGreaterElement(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(2 * n - 1, -1, -1):
        while stack and stack[-1] <= nums[i % n]:
            stack.pop()

        if stack:
            res[i % n] = stack[-1]

        stack.append(nums[i % n])

    return res

print('Задача 4.', circularNextGreaterElement([1, 2, 1]))