from collections import namedtuple

# Есть объекты со свойствами, которые задаются и не меняются. Поэтому для решения задачи выбрал именованный кортеж.

num_comp = int(input('сколько компаний?:  '))
comp_list = []
Company = namedtuple('Company', 'name q1 q2 q3 q4 profit')
sum_profit = 0

for i in range(num_comp):
    name = input('name: ')
    quarter_1 = float(input('profit_quarter_1:  '))
    quarter_2 = float(input('profit_quarter_2:  '))
    quarter_3 = float(input('profit_quarter_3:  '))
    quarter_4 = float(input('profit_quarter_4:  '))

    profit = quarter_1 + quarter_2 + quarter_3 + quarter_4
    sum_profit += quarter_1 + quarter_2 + quarter_3 + quarter_4
    company = Company(name, quarter_1, quarter_2, quarter_3, quarter_4, profit)
    comp_list.append(company)

average = sum_profit / num_comp
print(f'Средняя прибыль:  {average:.3f}', '\n')
more_av = []
less_av = []

for company in comp_list:
    if company.profit < average:
        less_av.append(company)
    else:
        more_av.append(company)

print('Их прибыль ВЫШЕ среднеей:')
for company in more_av:
    print(f'{company.name} - {company.profit}')

print('Их прибыль НИЖЕ среднеей:')
for company in less_av:
    print(f'{company.name} - {company.profit}')
