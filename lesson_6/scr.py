# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
"""
Переменные получим функцией dir(). Отсеем __такие__ имена. Из остальных сформируем список. Список объявлен
вне функций, чтобы не включать его память в общую, поэтому при проверке нужно комментить вызовы всех
функции, кроме проверяемой.
"""
import random
import sys
el_list = []


def show_size(elements):
    memory = 0
    for el in elements:
        print(f'type - {el.__class__}, size - {sys.getsizeof(el)}, odj - {el}')
        memory += sys.getsizeof(el)
    print(f'Memory - {memory}')


def func_1():
    int_l = int(input('левая граница (целое): '))
    int_r = int(input('правая граница (целое): '))
    fl_l = float(input('левая граница (вещ-е): '))
    fl_r = float(input('правая граница (вещ-е): '))
    str_l = input('первая буква: ')
    str_r = input('вторая буква: ')
    int_res = random.randint(int_l, int_r)
    fl_res = random.uniform(fl_l, fl_r)
    str_res = chr(random.randint(ord(str_l), ord(str_r) + 1))
    print(f'int - {int_res}, float - {fl_res}, str - {str_res}')

    print('\n', locals())
    for el_name in dir():
        if not el_name.startswith('__'):
            el_list.append(locals()[el_name])
    show_size(el_list)


"""
 {'int_l': 1, 'int_r': 10, 'fl_l': 1.0, 'fl_r': 10.0, 'str_l': 'a', 'str_r': 'f', 'int_res': 6, 'fl_res': 9.583729723903545, 'str_res': 'd'}
type - <class 'float'>, size - 24, odj - 1.0
type - <class 'float'>, size - 24, odj - 10.0
type - <class 'float'>, size - 24, odj - 9.583729723903545
type - <class 'int'>, size - 28, odj - 1
type - <class 'int'>, size - 28, odj - 10
type - <class 'int'>, size - 28, odj - 6
type - <class 'str'>, size - 50, odj - a
type - <class 'str'>, size - 50, odj - f
type - <class 'str'>, size - 50, odj - d
Memory - 306

Очень много переменных. От пользователя требуется ввод 6 значений. Отправим их сразу куда необходимо без 
дополнительных переменных
"""


def func_2():
    # int_l = int(input('левая граница (целое): '))
    # int_r = int(input('правая граница (целое): '))
    # fl_l = float(input('левая граница (вещ-е): '))
    # fl_r = float(input('правая граница (вещ-е): '))
    # str_l = input('первая буква: ')
    # str_r = input('вторая буква: ')
    int_res = random.randint(int(input('левая граница (целое): ')), int(input('правая граница (целое): ')))
    fl_res = random.uniform(float(input('левая граница (вещ-е): ')), float(input('правая граница (вещ-е): ')))
    str_res = chr(random.randint(ord(input('первая буква: ')), ord(input('вторая буква: ')) + 1))
    print(f'int - {int_res}, float - {fl_res}, str - {str_res}')

    print('\n', locals())
    for el_name in dir():
        if not el_name.startswith('__'):
            el_list.append(locals()[el_name])
    show_size(el_list)


"""
{'int_res': 9, 'fl_res': 6.246081521691226, 'str_res': 'c'}
type - <class 'float'>, size - 24, odj - 6.246081521691226
type - <class 'int'>, size - 28, odj - 9
type - <class 'str'>, size - 50, odj - c
Memory - 102

Уменьшаем количество переменных путем ввода значения сразу в функцию. Втрое уменьшаются затраты памяти. 
Можно отказаться и от оставшихся переменных, если результат рандомных функций отправить сразу в print или return, 
но код будет совсем не читаемым.
"""


def func_3():
    print(f"int - {random.randint(int(input('левая граница (целое): ')), int(input('правая граница (целое): ')))},"
          f" float - {random.uniform(float(input('левая граница (вещ-е): ')), float(input('правая граница (вещ-е): ')))},"
          f" str - {chr(random.randint(ord(input('первая буква: ')), ord(input('вторая буква: ')) + 1))}")

    print('\n', locals())
    for el_name in dir():
        if not el_name.startswith('__'):
            el_list.append(locals()[el_name])
    show_size(el_list)


"""
 {}
Memory - 0
Список переменных пуст. Разбив print на 3 строчки, можно прочесть код. Возможно, в некоторых случаях и этот способ 
окажется лучшим.
"""
"""
Вывод. Первый вариант мне не нравится из-за кучи переменных, которые используются один раз. Второй более компактный
и без мусора. Третий тоже хорош, не такой уж и громоздкий. Пока только предполагаю, что любая 
незначительная экономия памяти и скорости даст заметный рост производительности на больших данных.
"""


# func_1()
# func_2()
# func_3()
