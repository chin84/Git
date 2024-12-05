def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
   
print_params(12, 'function')
print_params(23, None, False)
print_params(21)
print_params()

print_params(b = 25) 
print_params(c = [1,2,3])

values_list =  [1, 'Word', True]
values_dict = {'a': 'zero', 'b': 3,'c': None}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]

print('Function print_params(*values_list_2, 42) is working')
