def not_sieve(find_num):
    """
    python -m timeit -n 1000 -s "import not_sieve" "not_sieve.not_sieve(100)"
    1000 loops, best of 5: 780 usec per loop

    python -m timeit -n 1000 -s "import not_sieve" "not_sieve.not_sieve(200)"
    1000 loops, best of 5: 3.47 msec per loop

    python -m timeit -n 1000 -s "import not_sieve" "not_sieve.not_sieve(300)"
    1000 loops, best of 5: 8.49 msec per loop

    Чем большее число ищем, тем больше вычислений нужно произвести. Время выполнения стремительно растет.
    Очевидно, нужно уменьшать количетство расчетов вводом дополнительных условий
    """
    # Простые числа 2 и 3 не перебрать в цикле с текущим условием. Вернем их отдельным кодом.
    if find_num == 1:
        return 2
    if find_num == 2:
        return 3
    # Следующее число 4 не простое, в цикле будет увеличено на 1
    val = 4
    # Вывели 2 и 3, уменьшаем счетчик
    find_num -= 2
    prime_num = True
    while True:
        # Увеличим на 1, получим следующее число для проверки. Нет смысла делить на все предшествующие числа.
        # Сузим диапазон val // 2 + 1
        val += 1
        for j in range(2, val // 2 + 1):
            if val % j == 0:
                # Если делится без остатка на любое предшествующее число, то число не простое, меняем флаг, выход
                prime_num = False
                break
        # Если флаг не поменялся, то число простое. Уменьшаем счетчик
        if prime_num:
            find_num -= 1
        # Если флаг менялся, то вернем обратно, чтобы алгоритм работал как раньше.
        prime_num = True
        # Если счетчик достиг нуля, то получили нужное число. Закончим цикл.
        if find_num == 0:
            break
    return val


def not_sieve_2(find_num):
    """
    В этом варианте отсеем четные числа и кратные 5. Видим многократный прирост скорости

    python -m timeit -n 1000 -s "import not_sieve" "not_sieve.not_sieve_2(100)"
    1000 loops, best of 5: 254 usec per loop

    python -m timeit -n 1000 -s "import not_sieve" "not_sieve.not_sieve_2(200)"
    1000 loops, best of 5: 954 usec per loop

    lesson_2>python -m timeit -n 1000 -s "import not_sieve" "not_sieve.not_sieve_2(300)"
    1000 loops, best of 5: 2.1 msec per loop
    """
    if find_num == 1:
        return 2
    if find_num == 2:
        return 3
    val = 4
    find_num -= 2
    prime_num = True
    while True:
        val += 1
        for j in range(3, val // 2 + 1):
            if val % 2 == 0 or val % 5 == 0:
                continue
            if val % j == 0:
                prime_num = False
                break
        if prime_num:
            find_num -= 1
        prime_num = True
        if find_num == 0:
            break
    return val


"""
Вывод.
Скорость выполнения алгоритма упирается в количество вычислений. В данном примере отсеяли очевидные
вычисления. Уверен, можно сократить вычисления еще больше. Знания математики помогли бы. Прошу написать свои идеи 
в замечаниях.
"""
