# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание
# к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = 0
for spam in array:
    if spam < 0:
        if spam < min_:
            min_ = spam
print(min_)
max_min = min_
for spam in array:
    if spam < 0 and spam > max_min:
        max_min = spam
print(f'Максимальное отрицательно - {max_min}')
