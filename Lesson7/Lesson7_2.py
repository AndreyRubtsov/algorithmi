# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def res_array(left_ar,right_ar):
    result=[]

    return result


def merge_sort(array):
    n = len(array)
    if n > 1:
        middle = int(len(array) / 2)
        left_ = merge_sort(array[:middle])
        right_ = merge_sort(array[middle:])
        return res_array(left_, right_)
    else:
        return array


# my_array = [random.random() * 50 for i in range(10)]
my_array = [random.randrange(-100, 99) for i in range(10)]
print(my_array)
merge_sort(my_array)
print(my_array)