# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
import random


def stone_sort(array):
    n = 1
    while n < len(array):
        flag = True
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = False
        if flag:
            break
        n += 1
        print(array)


my_array = [random.randrange(-100, 100) for i in range(10)]
print(my_array)
stone_sort(my_array)
print(my_array)
