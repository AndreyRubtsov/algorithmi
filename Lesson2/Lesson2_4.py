# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов
# (n) вводится с клавиатуры.

n = int(input("Введите количество элементов ряда чисел 1 -0.5 0.25 ... :"))
sum = 0
next = 1
for i in range(0, n):
    sum += next
    next *= -0.5

print("Сумма чисел ряда равна ", sum)
