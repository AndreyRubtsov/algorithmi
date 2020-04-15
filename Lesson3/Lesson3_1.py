# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
array2_99 = [i for i in range(2, 100)]
array2_9 = [i for i in range(2, 10)]

for j in array2_9:
    count = 0
    for i in array2_99:
        if i % j == 0:
            count += 1
    print(f'кратны {j} - {count}')



for q in range(2, 10):
    print(99//q)