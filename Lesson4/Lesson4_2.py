# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».Второй — без использования «Решета Эратосфена».
import timeit
import cProfile
import math

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



#нахождение n-го простого чисел
def isSimple(n):
    i = 2
    limit = int(math.sqrt(n))
    j = 0
    while i <= limit:
        if n % i == 0:
            j = 1
        i += 1
    return True if j == 0 else False

def simple(nn):
    a = []
    n=2
    while len(a) < nn:
        if isSimple(n):
            a.append(n)
        n += 1
    return a[-1]


print(timeit.timeit('simple(50)', number=100, globals=globals())) #0.020608320999599528
print(timeit.timeit('simple(100)', number=100, globals=globals()))#0.05859610800143855
print(timeit.timeit('simple(150)', number=100, globals=globals()))#0.11196539000047778
print(timeit.timeit('simple(200)', number=100, globals=globals()))#0.1835299419999501
print(timeit.timeit('simple(250)', number=100, globals=globals()))#0.26274313800058735
cProfile.run('simple(50)')
      # 228    0.000    0.000    0.000    0.000 Lesson4_2.py:37(isSimple)
      # 229    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      # 228    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
      #  50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('simple(100)')
      # 540    0.001    0.000    0.001    0.000 Lesson4_2.py:37(isSimple)
      # 541    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      # 540    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
      # 100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run('simple(150)')
      # 862    0.001    0.000    0.001    0.000 Lesson4_2.py:37(isSimple)
      # 863    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      # 862    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
      # 150    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('simple(200)')
      # 1222    0.002    0.000    0.002    0.000 Lesson4_2.py:37(isSimple)
      # 1223    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      # 1222    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
      #  200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('simple(250)')
      # 1582    0.003    0.000    0.003    0.000 Lesson4_2.py:37(isSimple)
      # 1583    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      # 1582    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
      #  250    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# Проверил 2 варианта алгоритма нахождения простых чисел. в первом случае использовалось решето Эратосфена
