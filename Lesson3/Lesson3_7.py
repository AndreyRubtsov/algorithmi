# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = array[0]
pos_min = 0
for spam in range(0, len(array)):
    if array[spam] < min_:
        min_ = array[spam]
        pos_min = spam
print(f'в данном массиве минимальное {min_} в позиции {pos_min}')

if pos_min == 0:
    min2_ = array[1]
    pos_min2 = 1
else:
    min2_ = array[0]
    pos_min2 = 0

for spam in range(0, len(array)):
    if spam != pos_min:
        if array[spam] < min2_:
            min2_ = array[spam]
            pos_min2 = spam

print(f'второе минимальное {min2_} в позиции {pos_min2}')
