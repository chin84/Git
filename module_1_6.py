my_dict = {'Fedya': 2014, 'Sonya': 2009, 'Pasha': 2008}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Fedya'])
my_dict['Sasha'] = 2002
print("New existing value: ", my_dict['Sasha'])
my_dict.update({'Dima': 2005,
                'Galya': 2006})
deleted_key = my_dict.pop('Dima')
print('Deleted value: ', deleted_key)
print('Modified Dictionary: ', my_dict)

my_list = [1, 2, 2, 'Yes', 'Yes', (1, 2, 2)]
my_set = set(my_list)
print('Set: ', my_set)
my_set.add('1')
my_set.add('[1, 2, 3.3, True, +, -, :')
print(my_set)
my_set.discard('[1, 2, 3.3, True, +, -, :')
print('Modfied Set: ', my_set)
