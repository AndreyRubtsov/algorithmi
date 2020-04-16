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

def er_fun(nn):
    a = []
    n=2
    while len(a)<nn:
        a=eratosphen(n)
        n+=1
    return a

def eratosphen2(n):
    n*=n
    a = [0] * n # создание массива с n количеством элементов

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
    return b[9]



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
print('*'*50)
print(timeit.timeit('eratosphen2(50)', number=100, globals=globals())) #0.05926470100166625
print(timeit.timeit('eratosphen2(100)', number=100, globals=globals()))#0.2578550779981015
print(timeit.timeit('eratosphen2(150)', number=100, globals=globals()))#0.5985802690011042
print(timeit.timeit('eratosphen2(200)', number=100, globals=globals()))#1.2683410179997736
print(timeit.timeit('eratosphen2(250)', number=100, globals=globals()))#1.9390846730020712
print('*'*50)
print(timeit.timeit('er_fun(50)', number=100, globals=globals())) #0.525912173998222
print(timeit.timeit('er_fun(100)', number=100, globals=globals()))#2.9953730419983913
print(timeit.timeit('er_fun(150)', number=100, globals=globals()))#7.948331477000465
print(timeit.timeit('er_fun(200)', number=100, globals=globals()))#16.32714142899931
print(timeit.timeit('er_fun(250)', number=100, globals=globals()))#27.786371258000145


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

cProfile.run('eratosphen2(50)')
      # 1    0.001    0.001    0.001    0.001 Lesson4_2.py:42(eratosphen2)
      # 367    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('eratosphen2(100)')
     # 1    0.003    0.003    0.003    0.003 Lesson4_2.py:42(eratosphen2)
     # 1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('eratosphen2(150)')
     # 1    0.007    0.007    0.007    0.007 Lesson4_2.py:42(eratosphen2)
     # 2515    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('eratosphen2(200)')
     # 1    0.011    0.011    0.011    0.011 Lesson4_2.py:42(eratosphen2)
     # 4203    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('eratosphen2(250)')
     # 1    0.017    0.017    0.017    0.017 Lesson4_2.py:42(eratosphen2)
     # 6275    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


cProfile.run('er_fun(50)')
     # 229    0.005    0.000    0.006    0.000 Lesson4_2.py:9(eratosphen)
     #    1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
     #  230    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     # 6383    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('er_fun(100)')
    # 541    0.033    0.000    0.034    0.000 Lesson4_2.py:9(eratosphen)
    #     1    0.000    0.000    0.034    0.034 {built-in method builtins.exec}
    #   542    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    # 30067    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
cProfile.run('er_fun(150)')
    # 863    0.082    0.000    0.085    0.000 Lesson4_2.py:9(eratosphen)
    #     1    0.000    0.000    0.086    0.086 {built-in method builtins.exec}
    #   864    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    # 70331    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
cProfile.run('er_fun(200)')
   # 1223    0.183    0.000    0.188    0.000 Lesson4_2.py:9(eratosphen)
   #      1    0.000    0.000    0.189    0.189 {built-in method builtins.exec}
   #   1224    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   # 133213    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
cProfile.run('er_fun(250)')
   # 1583    0.332    0.000    0.341    0.000 Lesson4_2.py:9(eratosphen)
   #      1    0.000    0.000    0.343    0.343 {built-in method builtins.exec}
   #   1584    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   # 213891    0.009    0.000    0.009    0.000 {method 'append' of 'list' objects}
# # Проверил 3 варианта алгоритма нахождения простых чисел. в первом случае(er_fun) использовалось решето Эратосфена
# и в цикле вызывался функция(eratosphen) для нахождения простого числа. Он оказался самим неудачным. После этого
# проверялся алгоритм где создавалось заведомо больший массив. Средние результаты за счет того что сложность на порядок
# меньше. Самым оптимальным оказался обычный перебор.
