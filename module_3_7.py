def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    #print(a, b, c, d) # разное кол-во аргументов


print_params()   # вызов без аргументов
print_params(1, 'строка')
print_params(1)
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [5, 'Yes', [7,8]]
values_dict = {'a': 7, 'b': 'строка', 'c': False}
def print_params(*values_list, **values_dict):
    print(*values_list)
    print(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)