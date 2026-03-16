import time
import random
import sys
from copy import deepcopy

sys.setrecursionlimit(10000)

# 1. O(1) - доступ к среднему элементу
def f01_access_middle(arr):
    return arr[len(arr) // 2]

# 2. O(log n) - бинарный поиск (массив должен быть отсортирован)
def f03_binary_search(arr, key):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# 3. O(n) - поиск максимума
def f07_find_max(arr):
    mx = arr[0]
    for x in arr:
        if x > mx:
            mx = x
    return mx

# 4. O(n log n) - сортировка слиянием
def f14_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = f14_merge_sort(arr[:mid])
    right = f14_merge_sort(arr[mid:])
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# 5. O(n^2) - пузырьковая сортировка (меняет исходный массив)
def f18_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 6. O(n^3) - наивный поиск тройки с суммой target
def f26_three_sum_naive(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return True
    return False

# 7. O(2^n) - рекурсивное число Фибоначчи
def f29_fib_naive(n):
    if n <= 1:
        return n
    return f29_fib_naive(n - 1) + f29_fib_naive(n - 2)

# 8. O(n!) - подсчёт всех перестановок (генерация)
def f30_count_perms(arr):
    def generate(a, l, r):
        if l == r:
            return 1
        count = 0
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            count += generate(a, l + 1, r)
            a[l], a[i] = a[i], a[l]
        return count
    copy_arr = arr[:]
    return generate(copy_arr, 0, len(copy_arr) - 1)

def measure_time(func, *args, repeat=1):
    start = time.perf_counter()
    for _ in range(repeat):
        result = func(*args)
    end = time.perf_counter()
    return (end - start) / repeat, result

def main():
    random.seed(42)
    results = {}

    # 1. f01_access_middle (O(1))
    print("f01_access_middle (O(1))...")
    sizes_01 = [100_000, 200_000, 300_000, 400_000]
    repeat_01 = 1_000_000
    times_01 = []
    for n in sizes_01:
        arr = [random.randint(0, 1000) for _ in range(n)]
        t, _ = measure_time(f01_access_middle, arr, repeat=repeat_01)
        times_01.append((n, t))
        print(f"  n = {n:10d}, время одного вызова = {t:.12f} сек")
    results['f01_access_middle'] = times_01
    print()

    # 2. f03_binary_search (O(log n))
    print("f03_binary_search (O(log n))...")
    sizes_03 = [1000, 10_000, 100_000, 1_000_000, 10_000_000]
    repeat_03 = 10_000
    times_03 = []
    for n in sizes_03:
        arr = [random.randint(0, n*10) for _ in range(n)]
        arr.sort()
        key = arr[n // 2]
        t, _ = measure_time(f03_binary_search, arr, key, repeat=repeat_03)
        times_03.append((n, t))
        print(f"  n = {n:10d}, время одного поиска = {t:.12f} сек")
    results['f03_binary_search'] = times_03
    print()

    # 3. f07_find_max (O(n))
    print("f07_find_max (O(n))...")
    sizes_07 = [1000, 10_000, 100_000, 1_000_000, 10_000_000]
    times_07 = []
    for n in sizes_07:
        arr = [random.randint(0, 1000) for _ in range(n)]
        t, _ = measure_time(f07_find_max, arr, repeat=1)
        times_07.append((n, t))
        print(f"  n = {n:10d}, время = {t:.6f} сек")
    results['f07_find_max'] = times_07
    print()

    # 4. f14_merge_sort (O(n log n)) - возвращает новый массив, не меняет исходный
    print("f14_merge_sort (O(n log n))...")
    sizes_14 = [1000, 5000, 10_000, 50_000, 100_000, 200_000]
    times_14 = []
    for n in sizes_14:
        arr = [random.randint(0, 1000) for _ in range(n)]
        t, _ = measure_time(f14_merge_sort, arr, repeat=1)
        times_14.append((n, t))
        print(f"  n = {n:10d}, время = {t:.6f} сек")
    results['f14_merge_sort'] = times_14
    print()

    # 5. f18_bubble_sort (O(n^2)) - изменяет массив, поэтому перед каждым замером создаём копию
    print("f18_bubble_sort (O(n^2))...")
    sizes_18 = [100, 500, 1000, 2000, 3000, 4000, 5000]  # для Python не больше 5000, иначе долго
    times_18 = []
    for n in sizes_18:
        original = [random.randint(0, 1000) for _ in range(n)]
        # Функция сортировки изменяет список, поэтому будем подавать копию
        arr_copy = original[:]
        t, _ = measure_time(f18_bubble_sort, arr_copy, repeat=1)
        times_18.append((n, t))
        print(f"  n = {n:10d}, время = {t:.6f} сек")
    results['f18_bubble_sort'] = times_18
    print()

    # 6. f26_three_sum_naive (O(n^3))
    print("f26_three_sum_naive (O(n^3))...")
    sizes_26 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    target = 0
    times_26 = []
    for n in sizes_26:
        arr = [random.randint(-500, 500) for _ in range(n)]
        t, _ = measure_time(f26_three_sum_naive, arr, target, repeat=1)
        times_26.append((n, t))
        print(f"  n = {n:10d}, время = {t:.6f} сек")
    results['f26_three_sum_naive'] = times_26
    print()

    # 7. f29_fib_naive (O(2^n))
    print("f29_fib_naive (O(2^n))...")
    sizes_29 = [10, 15, 20, 25, 30, 35, 40]
    times_29 = []
    for n in sizes_29:
        t, _ = measure_time(f29_fib_naive, n, repeat=1)
        times_29.append((n, t))
        print(f"  n = {n:10d}, время = {t:.6f} сек")
    results['f29_fib_naive'] = times_29
    print()

    # 8. f30_count_perms (O(n!))
    print("f30_count_perms (O(n!))...")
    sizes_30 = [4, 5, 6, 7, 8, 9, 10, 11]
    times_30 = []
    for n in sizes_30:
        arr = list(range(n))
        t, _ = measure_time(f30_count_perms, arr, repeat=1)
        times_30.append((n, t))
        print(f"  n = {n:10d}, время = {t:.6f} сек")
    results['f30_count_perms'] = times_30
    print()

    for func_name, data in results.items():
        print(f"\n{func_name}:")
        print("    n        время (сек)")
        for n, t in data:
            print(f"{n:8d}    {t:.15f}")

if __name__ == "__main__":
    main()