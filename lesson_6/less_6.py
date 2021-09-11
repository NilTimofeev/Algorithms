import sys
print(sys.version, sys.platform)


def show_size(x, level=0):
    print('\t' * level, f'type - {x.__class__}, size - {sys.getsizeof(x)}, odj - {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, '__items__'):
            for xx in x.items():
                show_size(x, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(x, level + 1)


print(locals().keys())
