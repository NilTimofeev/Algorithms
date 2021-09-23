from binarytree import bst


def search(bin_search_tree, number, path=''):

    if bin_search_tree.value == number:
        return f'Число {number} найдено по пути: \n{path}'

    if number < bin_search_tree.value and bin_search_tree.left is not None:
        return search(bin_search_tree.left, number, path=f'{path}\nШаг влево')

    if number > bin_search_tree.value and bin_search_tree.right is not None:
        return search(bin_search_tree.right, number, path=f'{path}\nШаг вправо')

    return f'Число отсутствует'


bt = bst(height=5, is_perfect=False)
print(bt)

num = int(input('введите число:  '))
print(search(bt, num))

