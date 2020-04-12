# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из
# этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным
# или равносторонним.

print("Введите длины трех отрезков для определения возможностит существования треугольника  ")
a = float(input("Длина первого отрезка: "))
b = float(input("Длина второго отрезка: "))
c = float(input("Длина третьего отрезка: "))


if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print('Такой трeугольник не может существовать!')
elif a != b and a != c and b != c:
    print('Треугольник разносторонний')
elif a == b == c:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')