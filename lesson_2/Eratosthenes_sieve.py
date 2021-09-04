"""
Алгоритм "решето Эратосфена" заключается в поиске простых чисел до некоторого целого числа.
Поэтому определим это число сразу. И номер искомого простого числа выберем из допустимых.
Если простые числа ищем до 100, то получим 25 простых чисел. До 1000 - 168"
1 вариант. Решение из урока. Только будем искать одно число, а не весь список.
2 вариант. Заменим цикл while на for и сравним.
3 вариант. Попробуем найти весь список чисел и получить искомое из него.
"""
import timeit
import cProfile


def func_sieve(find_num):
    """
    В этом варианте находим очередное простое число и уменьшаем значение счетчика. Как только счетчик обнулился,
    возвращаем найденное простое число.

    python -m timeit -n 1000 -s "import Eratosthenes_sieve" "Eratosthenes_sieve.func_sieve(100)"
    1000 loops, best of 5: 507 usec per loop

    python -m timeit -n 1000 -s "import Eratosthenes_sieve" "Eratosthenes_sieve.func_sieve(200)"
    1000 loops, best of 5: 577 usec per loop

    python -m timeit -n 1000 -s "import Eratosthenes_sieve" "Eratosthenes_sieve.func_sieve(300)"
    1000 loops, best of 5: 649 usec per loop
    """
    num = 2000
    # find_num = 20
    num_list = [i for i in range(0, num)]
    num_list[1] = 0
    for i in range(2, num):
        if num_list[i] != 0:
            j = i + i
            find_num -= 1
            if find_num == 0:
                # print(num_list[i])
                return num_list[i]
            while j < num:
                num_list[j] = 0
                j += i
    # res_list = [num for num in num_list if num > 0]
    # print(res_list)
    # print(len(res_list))


def func_sieve_2(find_num):
    """
    Заменим цикл while на for. Получим более наглядное и компактное написание. Сравним время выполнения

    python -m timeit -n 1000 -s "import Eratosthenes_sieve" "Eratosthenes_sieve.func_sieve_2(100)"
    1000 loops, best of 5: 363 usec per loop

    python -m timeit -n 1000 -s "import Eratosthenes_sieve" "Eratosthenes_sieve.func_sieve_2(200)"
    1000 loops, best of 5: 447 usec per loop

    python -m timeit -n 1000 -s "import Eratosthenes_sieve" "Eratosthenes_sieve.func_sieve_2(300)"
    1000 loops, best of 5: 518 usec per loop
    """
    num = 2000
    # find_num = 20
    num_list = [i for i in range(0, num)]
    num_list[1] = 0
    for i in range(2, num):
        if num_list[i] != 0:
            find_num -= 1
            if find_num == 0:
                return num_list[i]
            for j in range(i + i, num, i):
                num_list[j] = 0


def func_sieve_3(find_num):
    """
    Сформируем список простых чисел, как в решении урока, и возьмем из него нужное значение.

    python -m timeit -n 1000 -s "import Eratosthenes_sieve" "Eratosthenes_sieve.func_sieve_2(100)"
    1000 loops, best of 5: 549 usec per loop

    python -m timeit -n 1000 -s "import Eratosthenes_sieve" "Eratosthenes_sieve.func_sieve_2(200)"
    1000 loops, best of 5: 555 usec per loop

    python -m timeit -n 1000 -s "import Eratosthenes_sieve" "Eratosthenes_sieve.func_sieve_2(300)"
    1000 loops, best of 5: 562 usec per loop
    """
    num = 2000
    num_list = [i for i in range(0, num)]
    num_list[1] = 0
    for i in range(2, num):
        if num_list[i] != 0:
            for j in range(i + i, num, i):
                num_list[j] = 0
    res_list = [num for num in num_list if num > 0]
    return res_list[find_num]


"""
Вывод.
Цикл for выполняется быстрее while. В обоих случаях время выполнения изменяется пропорционально числу итераций.

В случае сохранения в список всех значений цикл отработает полностью. Поэтому время выполнения программы одинаково
всегда. И больше памяти нужно для хранения списка результата.
"""
