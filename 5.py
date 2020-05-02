"""
5. Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.
"""

abc_number = int(input('Введите номер буквы в алфавите: '))

abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

if abc_number <= len(abc_list):
    print(f'{abc_list[abc_number - 1]} - буква под номером {abc_number}')
else:
    print(f'Введено число превышающее количество букв в алфавите ({len(abc_list)})')