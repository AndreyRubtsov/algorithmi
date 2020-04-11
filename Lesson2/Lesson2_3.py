# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на
# экран. Например, если введено число 3486, то надо вывести число 6843


n = int(input("Введите число: "))
new_n = ''


def find_new_n(input_n):
    global new_n
    if input_n > 0.9:
        i = input_n % 10
        new_n += str(i)
        find_new_n(int(input_n / 10))


find_new_n(n)
print("Обратное число - ", new_n)
