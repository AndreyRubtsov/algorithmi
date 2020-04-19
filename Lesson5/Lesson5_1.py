# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

n = int(input("Количество предприятий: "))
sum_ = 0
Companys = namedtuple('Companys', 'name,q1,q2,q3,q4,firm_avg')
company = {}

for i in range(n):
    firm_name = input("Bведите название фирмы:")
    v_q1 = float(input("Bведите прибыль за 1 квартал:"))
    v_q2 = float(input("Bведите прибыль за 2 квартал:"))
    v_q3 = float(input("Bведите прибыль за 3 квартал:"))
    v_q4 = float(input("Bведите прибыль за 4 квартал:"))

    firm_avg = float(v_q1 + v_q2 + v_q3 + v_q4) / 4
    sum_ += firm_avg
    company[i] = Companys(firm_name, v_q1, v_q2, v_q3, v_q4, firm_avg)

avg_all = sum_ / n

print("Прибыль выше среднего у следующих предприятий:")
for i in range(n):
    if company[i].firm_avg > avg_all:
        print(company[i].name)
print("Прибыль ниже среднего у следующих предприятий:")
for i in range(n):
    if company[i].firm_avg < avg_all:
        print(company[i].name)
