# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на
# экран. Например, если введено число 3486, то надо вывести число 6843
import timeit
def find_new_n1(input_n):
    new_n = ''
    if input_n > 0.9:
        i = input_n % 10
        new_n += str(i)
        new_n += str(find_new_n1(int(input_n / 10)))
    return new_n

def find_new_n2(input_n):
    new_n = ''
    while input_n > 0.9:
        i = input_n % 10
        new_n += str(i)
        input_n = int(input_n / 10)
    return new_n

def find_new_n3(input_n):
    new_n = 0
    while input_n > 0:
        new_n = new_n * 10 + input_n % 10
        input_n = input_n // 10
    return new_n



print(timeit.timeit('find_new_n1(141279427587812313441341434342424)', number=100, globals=globals()))
print(timeit.timeit('find_new_n2(141279427587812313441341434342424)', number=100, globals=globals()))
print(timeit.timeit('find_new_n3(141279427587812313441341434342424)', number=100, globals=globals()))