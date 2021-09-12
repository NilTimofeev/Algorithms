# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
import random
import sys

print(sys.version, sys.platform)
"""
3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] win32
Словарь переменых плучим функцией locals(). Вызовем show_size, пердав в нее словарь.
Рассмотрим 3 варианта решения, в которых будем сокращать количество пременных, делая код компактнее, но менее читаемым.
В конце сравним результаты.
"""


def show_size(elements):
    memory = 0
    for el in elements.items():
        print(f'type - {el[1].__class__},\t size - {sys.getsizeof(el[1])},\t {el[0]} = {el[1]}')
        memory += sys.getsizeof(el[1])
    print(f'Memory = {memory}')


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

    show_size(locals())


"""
type - <class 'int'>,	 size - 28,	 int_l = 1
type - <class 'int'>,	 size - 28,	 int_r = 10
type - <class 'float'>,	 size - 24,	 fl_l = 1.0
type - <class 'float'>,	 size - 24,	 fl_r = 10.0
type - <class 'str'>,	 size - 50,	 str_l = a
type - <class 'str'>,	 size - 50,	 str_r = f
type - <class 'int'>,	 size - 28,	 int_res = 2
type - <class 'float'>,	 size - 24,	 fl_res = 7.98350967229811
type - <class 'str'>,	 size - 50,	 str_res = g
Memory = 306

Очень много переменных. От пользователя требуется ввод 6 значений. В следующем варианте отправим их сразу куда 
необходимо без дополнительных переменных
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

    show_size(locals())


"""
type - <class 'int'>,	 size - 28,	 int_res = 5
type - <class 'float'>,	 size - 24,	 fl_res = 7.399131859799863
type - <class 'str'>,	 size - 50,	 str_res = c
Memory = 102

Уменьшаем количество переменных путем ввода значения сразу в функцию. Втрое уменьшаются затраты памяти. 
Можно отказаться и от оставшихся переменных, если результат рандомных функций отправить сразу в print или return.
Сделаем это в следующем примере.
"""


def func_3():
    print(f"int - {random.randint(int(input('левая граница (целое): ')), int(input('правая граница (целое): ')))},"
          f" float - {random.uniform(float(input('левая граница (вещ-е): ')), float(input('правая граница (вещ-е): ')))},"
          f" str - {chr(random.randint(ord(input('первая буква: ')), ord(input('вторая буква: ')) + 1))}")

    show_size(locals())


"""
Memory = 0

Список переменных пуст. Разбив print на 3 строчки, можно прочесть код. Возможно, в некоторых случаях и этот способ 
окажется лучшим.
"""
"""
Вывод. Первый вариант мне не нравится из-за кучи переменных, которые используются один раз. Второй более компактный
и без мусора. Третий тоже хорош, не такой уж и громоздкий. Разница в загруженности памяти не ощутима на такой простой 
программе, но в каких-то случаях третий вариант, думаю, допустим. 
"""


func_1()
func_2()
func_3()
