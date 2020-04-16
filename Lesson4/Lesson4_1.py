# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на
# экран. Например, если введено число 3486, то надо вывести число 6843
import timeit
import cProfile


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


test_num1 = 141279
test_num2 = 141279427587812
test_num3 = 141279427587812313441341434342424
test_num4 = 1412794275878123134413414343424242378942111473848924780478934
test_num5 = 14127942758781231344134143434242423843193405783056786718554897645893589368979349593456893445

print(timeit.timeit('find_new_n1(test_num1)', number=100, globals=globals()))  # 0.00035394699989410583
print(timeit.timeit('find_new_n1(test_num2)', number=100, globals=globals()))  # 0.0008104930000172317
print(timeit.timeit('find_new_n1(test_num3)', number=100, globals=globals()))  # 0.0019438470001205133
print(timeit.timeit('find_new_n1(test_num4)', number=100, globals=globals()))  # 0.003921147000028213
print(timeit.timeit('find_new_n1(test_num5)', number=100, globals=globals()))  # 0.006225735000043642
print('*' * 50)
print(timeit.timeit('find_new_n2(test_num1)', number=100, globals=globals()))  # 0.00020221999989189499
print(timeit.timeit('find_new_n2(test_num2)', number=100, globals=globals()))  # 0.0005359530000532686
print(timeit.timeit('find_new_n2(test_num3)', number=100, globals=globals()))  # 0.0014482999999927415
print(timeit.timeit('find_new_n2(test_num4)', number=100, globals=globals()))  # 0.002882936000105474
print(timeit.timeit('find_new_n2(test_num5)', number=100, globals=globals()))  # 0.005099989999962418
print('*' * 50)
print(timeit.timeit('find_new_n3(test_num1)', number=100, globals=globals()))  # 6.711100013490068e-05
print(timeit.timeit('find_new_n3(test_num2)', number=100, globals=globals()))  # 0.00019107000002804853
print(timeit.timeit('find_new_n3(test_num3)', number=100, globals=globals()))  # 0.0004983629999060213
print(timeit.timeit('find_new_n3(test_num4)', number=100, globals=globals()))  # 0.000932906000116418
print(timeit.timeit('find_new_n3(test_num5)', number=100, globals=globals()))  # 0.001932124999939333
test_num1 = (141279*1231231232312312312)**2
test_num2 = (41279427587812*1231231232312312312)**2
test_num3 = (41279427587812313441341434342424*1231231232312312312)**2
test_num4 = (1412794275878123134413414343424242378942111473848924780478934*1231231232312312312)**2
cProfile.run('find_new_n1(test_num1)')#48/1    0.000    0.000    0.000    0.000 Lesson4_1.py:7(find_new_n1)
cProfile.run('find_new_n1(test_num2)')#65/1    0.000    0.000    0.000    0.000 Lesson4_1.py:7(find_new_n1)
cProfile.run('find_new_n1(test_num3)')#101/1    0.000    0.000    0.000    0.000 Lesson4_1.py:7(find_new_n1)
cProfile.run('find_new_n1(test_num4)')#236/1    0.000    0.000    0.000    0.000 Lesson4_1.py:7(find_new_n1)
print('*' * 50)
cProfile.run('find_new_n2(test_num1)')#1    0.000    0.000    0.000    0.000 Lesson4_1.py:16(find_new_n2)
cProfile.run('find_new_n2(test_num2)')#1    0.000    0.000    0.000    0.000 Lesson4_1.py:16(find_new_n2)
cProfile.run('find_new_n2(test_num3)')#1    0.000    0.000    0.000    0.000 Lesson4_1.py:16(find_new_n2)
cProfile.run('find_new_n2(test_num4)')#1    0.000    0.000    0.000    0.000 Lesson4_1.py:16(find_new_n2)
print('*' * 50)
cProfile.run('find_new_n3(test_num1)')#1    0.000    0.000    0.000    0.000 Lesson4_1.py:25(find_new_n3)
cProfile.run('find_new_n3(test_num2)')#1    0.000    0.000    0.000    0.000 Lesson4_1.py:25(find_new_n3)
cProfile.run('find_new_n3(test_num3)')#1    0.000    0.000    0.000    0.000 Lesson4_1.py:25(find_new_n3)
cProfile.run('find_new_n3(test_num4)')#1    0.000    0.000    0.000    0.000 Lesson4_1.py:25(find_new_n3)

