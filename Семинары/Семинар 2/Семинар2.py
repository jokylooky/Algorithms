# Скользящее окно

def fixed_window(arr, k) -> None:
    n = len(arr)
    if n < k:
        return None

    # 1. Инициализируем первое окна
    window_sum = sum(arr[:k])
    best = window_sum

    # 2. Сдвигаем окно: убираем левый, добавляем правый
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        best = max(best, window_sum)

    return best