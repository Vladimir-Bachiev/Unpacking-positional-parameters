def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print('\33[1;33mprint_params(): \33[0m', end='')
print_params()  # без аргументов, используем значения по умолчанию

print('\33[1;33mprint_params(2): \33[0m', end='')
print_params(2)  # один аргумент, используем значения по умолчанию для b и c

print('\33[1;33mprint_params(2, новая_строка): \33[0m', end='')
print_params(2, 'новая_строка')  # два аргумента, используем значение по умолчанию для c

print('\33[1;33mprint_params(2, "новая_строка", False): \33[0m', end='')
print_params(2, 'новая_строка', False)  # три аргумента, без значений по умолчанию

print('\33[1;33mprint_params(b=25): \33[0m', end='')
print_params(b=25)  # именованный аргумент для b

print('\33[1;33mprint_params(c=[1, 2, 3]): \33[0m', end='')
print_params(c=[1, 2, 3])  # именованный аргумент для c

values_list = [4, 'другая_строка', False]
values_dict = {'a': 5, 'b': 'просто_строка', 'c': None}
print()
print("\33[1;34mvalues_list = [4, 'другая_строка', False]")
print("mvalues_dict = {'a': 5, 'b': 'просто_строка', 'c': None} \33[0m")

print('\33[1;33mprint_params(*values_list): \33[0m', end='')
print_params(*values_list)  # Распаковка списка

print('\33[1;33mprint_params(**values_dict): \33[0m', end='')
print_params(**values_dict)  # Распаковка словаря

values_list_2 = [54.32, 'Строка']
print()
print("\33[1;34mvalues_list_2 = [54.32, 'Строка']\33[0m")
print('\33[1;33mprint_params(*values_list_2, 42): \33[0m', end='')
print_params(*values_list_2, 42)
