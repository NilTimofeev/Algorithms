# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
first_letter = input('введите букву: ')
second_letter = input('и еще одну: ')
uni_num_f = ord(first_letter)
uni_num_s = ord(second_letter)
print(f'Буква {first_letter} под номером {uni_num_f - 96}. '
      f'А буква {second_letter} под номером {uni_num_s - 96}')
print(f'Между ними {abs(uni_num_s - uni_num_f) - 1} букв')
