# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = array[0]
for spam in array:
    if spam < min_:
        min_ = spam
print(min_)

for eggs in array:
    if eggs < min_:
        min_ = eggs
print(min_)
