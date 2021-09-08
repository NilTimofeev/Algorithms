from collections import namedtuple
num_comp = 2
res = []
Company = namedtuple('Company', 'name quarter_1 quarter_2 quarter_3 quarter_4')
sum_profit = 0

for i in range(num_comp):
    name = input('name: ')
    quarter_1 = input('profit_quarter_1:  ')
    quarter_2 = input('profit_quarter_2:  ')
    quarter_3 = input('profit_quarter_3:  ')
    quarter_4 = input('profit_quarter_4:  ')
    company = Company('name', quarter_1, quarter_2, quarter_3, quarter_4)
    res.append(company)

    sum_profit += quarter_1 + quarter_2 + quarter_3 + quarter_4
    print(company)

average = sum_profit / num_comp

for i in range(num_comp):
    comp_profit = res[i].quarter_1 + res[i].quarter_2 + res[i].quarter_3 + res[i].quarter_4
