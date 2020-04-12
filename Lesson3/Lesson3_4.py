# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = 0
num_count = 1

for j in array:
    count = 0
    for i in range(0, len(array)):
        if array[i] == j:
            count += 1
    print(count, j)
    if count > num_count:
        num_count = count
        num = j
if num:
    print(f'В данном массиве {num} имеет {num_count} повторений(я)')
else:
    print("Одинаковое количество повторений")
