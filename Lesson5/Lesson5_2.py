# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение
# - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


def hex_sum(num_a, num_b):
    a = deque(num_a.upper())
    b = deque(num_b.upper())

    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                'C': 12, 'D': 13, 'E': 14, 'F': 15, 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    new_level = 0
    result = deque()

    # выравниваем длину
    if len(a) > len(b):
        while len(a) != len(b):
            b.appendleft('0')
    if len(b) > len(a):
        while len(a) != len(b):
            a.appendleft('0')

    while a:
        a_last = hex_dict[a.pop()]
        b_last = hex_dict[b.pop()]
        sum_last = a_last + b_last + new_level
        new_level = 0
        if sum_last > 15:
            new_level = 1
        result.appendleft(hex_dict[sum_last % 16])
    if new_level:
        result.appendleft('1')
    str = ''
    for i in result:
        str += i

    return str


my_a = input('Введите первое число:')
my_b = input('Введите второе число:')
print('Сумма чисел: ', hex_sum(my_a, my_b))
