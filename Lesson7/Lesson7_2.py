# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def res_array(left_ar, right_ar):
    result = []
    # позиции левого и правого массива left array index, right array index
    lai = 0
    rai = 0
    for i in range(len(left_ar) + len(right_ar)):
        if lai < len(left_ar) and rai < len(right_ar):
            if left_ar[lai] <= right_ar[rai]:
                result.append(left_ar[lai])
                lai += 1
            else:
                result.append(right_ar[rai])
                rai += 1
        # «Прицепление» остатка.
        elif lai == len(left_ar):
            result.append(right_ar[rai])
            rai += 1
        elif rai == len(right_ar):
            result.append(left_ar[lai])
            lai += 1

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


my_array = [random.random() * 50 for i in range(10)]

print(my_array)
b = merge_sort(my_array)
print(b)
