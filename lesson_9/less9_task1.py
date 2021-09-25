import hashlib
# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
# не решённой.


def count_sub_str(s):

    hashes = set()

    for i in range(len(s) + 1):
        for j in range(i + 1, len(s)+1):
            hash_s = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            hashes.add(hash_s)

    # удалить хеш целой строки, если важны значения. или минус 1 в return, если важно только количество
    hashes.discard(hashlib.sha1(s.encode('utf-8')).hexdigest())

    return len(hashes)


st = 'logitech'
print(count_sub_str(st))
