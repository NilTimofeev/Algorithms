import sys
import random


def show_size(elements):
    memory = 0
    for el in elements.items():
        print('type - {},\t size - {},\t {} = {}'.format(el[1].__class__, sys.getsizeof(el[1]), el[0], el[1]))
        memory += sys.getsizeof(el[1])
    print(f'Memory = {memory}')


def func_1():
    int_l = 1
    int_r = 10
    fl_l = 1.0
    fl_r = 10.0
    str_l = 'a'
    str_r = 'f'
    int_res = random.randint(int_l, int_r)
    fl_res = random.uniform(fl_l, fl_r)
    str_res = chr(random.randint(ord(str_l), ord(str_r) + 1))
    print(f'int - {int_res}, float - {fl_res}, str - {str_res}')

    show_size(locals())

func_1()
