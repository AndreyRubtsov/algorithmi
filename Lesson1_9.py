# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print("Введите 3 числа")
a = input("Первое: ")
b = input("Второе: ")
c = input("Третье: ")

print(a, b, c)

if a > b:
    if a > c:
        if b > c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if a > c:
        print(a)
    else:
        if b > c:
            print(c)
        else:
            print(b)
