import functools
import timeit
import cProfile

# выполнил млн раз по умолчанию
#print(timeit.timeit('x = 2 + 2'))

# python -m timeit -n 1000 -s "import test"

@functools.lru_cache()

def func(num):
    num_list = [i for i in range(0, num + 1)]


# def func(num):
#     num_list = []
#     for i in range(0, num + 1):
#         num_list.append(i)

cProfile.run(func(100))
