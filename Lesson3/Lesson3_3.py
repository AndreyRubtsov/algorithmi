# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = array[0]
min_ = array[0]
pos_min = 0
pos_max = 0

# находим позиции максимального и минимального
for i in range(0, len(array)):
    if array[i] > max_:
        max_ = array[i]
        pos_max = i
    if array[i] < min_:
        min_ = array[i]
        pos_min = i

array[pos_max] = min_
array[pos_min] = max_
print(array)
