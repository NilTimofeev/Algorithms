import hashlib


# 1. сравнение строк
# def is_eq_str(a: str, b: str, verbose=False) -> bool:
#     assert len(a) > 0 and len(b) > 0, 'строки не должны быть пустые'
#
#     # получаем хеш строк. в ютф8 конверт и получаем байт-строки. их в алгоритм сха1 передали
#     # а результат в шестнадцатеричный формат
#     ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
#     hb = hashlib.sha1(b.encode('utf-8')).hexdigest()
#
#     if verbose:
#         print(f'hash1 = {ha}\nhash2 = {hb}')
#
#     return ha == hb
#
#
# s_1 = input('str 1:  ')
# s_2 = input('str 2:  ')
#
# print(f'строки одинаковые' if is_eq_str(s_1, s_2, True) else 'строки разные')


# 2. поиск подстроки в строке
def Rabin_Karp(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'строки не должны быть пустые'
    assert len(s) >= len(subs) > 0, 'подстрока не должна быть длиннее строки'

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            return i
    return -1


st = input('str:  ')
sub_s = input('sub_str:  ')
pos = Rabin_Karp(st, sub_s)

print(f'подстрока в позиции {pos}' if pos != -1 else 'not found')

