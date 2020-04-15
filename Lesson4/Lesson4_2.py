# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».Второй — без использования «Решета Эратосфена».
import timeit
import cProfile

# решето эратосфена
def eratosphen(n):
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1
    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b

def simple(n):
    a = []
    for k in range(2, n):
        i = 2
        j = 0
        while i ** 2 <= k and j != 1:
            if k % i == 0:
                j = 1
            i += 1
        if j != 1:
            a.append(k)
    return a


print(timeit.timeit('eratosphen(200)', number=100, globals=globals()))   # 0.004108042001462309
print(timeit.timeit('eratosphen(400)', number=100, globals=globals()))   # 0.008882021000317764
print(timeit.timeit('eratosphen(800)', number=100, globals=globals()))   # 0.019219728997995844
print(timeit.timeit('eratosphen(1600)', number=100, globals=globals()))  # 0.03777281300062896
print(timeit.timeit('eratosphen(3200)', number=100, globals=globals()))  # 0.07924962900142418
print('*' * 50)
print(timeit.timeit('simple(200)', number=100, globals=globals()))       # 0.017867424998257775
print(timeit.timeit('simple(400)', number=100, globals=globals()))       # 0.0440833240027132
print(timeit.timeit('simple(800)', number=100, globals=globals()))       # 0.10396033799770521
print(timeit.timeit('simple(1600)', number=100, globals=globals()))      # 0.2517929079986061
print(timeit.timeit('simple(3200)', number=100, globals=globals()))      # 0.6212756520035327
print('_' * 50)
cProfile.run('eratosphen(10000)')
cProfile.run('eratosphen(20000)')
cProfile.run('eratosphen(40000)')
cProfile.run('eratosphen(80000)')
cProfile.run('eratosphen(160000)')
print('*' * 50)
cProfile.run('simple(10000)')
cProfile.run('simple(20000)')
cProfile.run('simple(40000)')
cProfile.run('simple(80000)')
cProfile.run('simple(160000)')