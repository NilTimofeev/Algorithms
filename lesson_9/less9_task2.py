from collections import Counter

"""
1. Частота вхождения каждого символа в строку. Counter посчитает за нас и сформирует очередь, где приоритет - частота
входжения с втроку символа. Только она будет развернутой, поэтому начнем проходить с конца.
2. Строим дерево. Нужно связывать пару елементов в узел. Будем создавать объект MyNode из примера в уроке. 
Добавим его в очередь. Объект займет правильное место, т.к. очередь - Counter. Удалим из очереди элементы, которые 
связали узлом. Повторяем операции до тех пор, пока длина очереди не будет равна одному, получим корень дерева
"""


class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree(string):

    cnt = Counter(string)

    while len(cnt) != 1:
        node = Node(None)
        two_node = cnt.most_common()[-2::]

        if isinstance(two_node[1][0], str):
            node.left = Node(two_node[1][0])
        else:
            node.left = two_node[1][0]

        if isinstance(two_node[0][0], str):
            node.right = Node(two_node[0][0])
        else:
            node.right = two_node[0][0]

        del cnt[two_node[0][0]]
        del cnt[two_node[1][0]]

        cnt[node] = two_node[1][1] + two_node[0][1]

    # print(tuple(*cnt.items())[0])
    return tuple(*cnt.items())[0]


"""
3. Нужно составить таблицу кодов всех символов. Рекурсивно пройдем по веткам дерева, пока не достигнем листьев, там 
будут строковые значение. Пока движемся к листку, добавляем нули и единицы к коду.
"""


def codes_table(tr, table={}, code=''):
    if isinstance(tr.data, str):
        table[tr.data] = code
        return table

    codes_table(tr.left, table, f'{code}0')
    codes_table(tr.right, table, f'{code}1')

    return table


def encoding_str(codes_tab, st):
    encoded_str = ''
    for i in range(len(st)):
        # делаю с пробелом, чтобы было удобнее проверить
        encoded_str = f'{encoded_str}{codes_tab[st[i]]} '

    return encoded_str


s = 'beep boop beer!'
print(s)
tr = tree(s)
table = codes_table(tr)
print(table)
print(encoding_str(table, s))
