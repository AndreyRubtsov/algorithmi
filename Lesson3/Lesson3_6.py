# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = array[0]
min_ = array[0]
pos_min = 0
pos_max = 0
sum_ = 0

# находим позиции максимального и минимального
for i in range(0, len(array)):
    if array[i] > max_:
        max_ = array[i]
        pos_max = i
    if array[i] < min_:
        min_ = array[i]
        pos_min = i

# если максимальное стоит раньше минимального, то запомненные позиции меняем местами
if pos_max < pos_min:
    i = pos_min
    pos_min = pos_max
    pos_max = i

# подсчет
if pos_max - pos_min == 1:
    print("Стоят рядом, нет возможности посчитать сумму")
else:
    for i in range(pos_min + 1, pos_max):
        sum_ += array[i]
    print(f'Сумма чисел, находящаяся между {max_} и {min_} равна {sum_}')
