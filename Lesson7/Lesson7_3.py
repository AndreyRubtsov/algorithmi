# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
import random


def mediana(array):
    result = 0

    for i in array:
        gt = 0
        lt = 0
        for j in range(len(array)):
            if i > array[j]:
                gt += 1
            elif i < array[j]:
                lt += 1
            # print(i,gt,lt)
        if gt == lt:
            result = i
    return result


var_m = int(input('Input m:'))
my_array = [random.randint(-100, 99) for i in range(2 * var_m + 1)]
print(my_array)
print('Медиана массива - ', mediana(my_array))
print("Для проверки:\n", sorted(my_array))
