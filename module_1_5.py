immutable_var = (1, 1.1, 'string', True)
print(immutable_var)
# immutable_var[0] = 2  -> Невозможно внести изменения в неизменяемую структуру данных
# print(immutable_var)
mutable_list = [1, 1.1, 'string', True]
mutable_list[3] = False
print(mutable_list)