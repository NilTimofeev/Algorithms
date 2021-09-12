import sys
import random
el_list = []



def show_size(elements):
    memory = 0
    for el in elements:
        print(f'type - {el.__class__}, size - {sys.getsizeof(el)}, odj - {el}')
        memory += sys.getsizeof(el)
    print(f'Memory - {memory}')


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

    print('\n', locals())
    print('\n', dir())

    for el in locals().items():
        #print(f'type - {el[1].__class__}, size - {sys.getsizeof(el[1])}, odj - {el[0]}')
        print('type - {:15s}, size - {}, odj - {}'.format(el[1].__class__, sys.getsizeof(el[1]), el[0]))

func_1()