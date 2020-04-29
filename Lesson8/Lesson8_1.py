# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.Примечание: в сумму не включаем пустую строку
# и строку целиком.
import hashlib


def find_subs(some_string):
    hash_subs = []
    for i in range(len(some_string)):
        for j in range(i + 1, len(some_string) + 1):
            if some_string != some_string[i:j]:
                hash_s = hashlib.sha512(some_string[i:j].encode('utf-8')).hexdigest()
                if hash_s not in hash_subs:
                    hash_subs.append(hash_s)

    for i in hash_subs:
        print(i)

    return len(hash_subs)


my_string = 'sova'

print('В искомой строке ', find_subs(my_string), ' разных подстрок')
