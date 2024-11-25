immutable_var = (1, 2, True, 'False',[1, 2, 3])
print(immutable_var)
''' immutable_var[0] = '1'
Кортеж - неизменяемый тип данных, 
в самом кортеже могут находится изменяемые типы данных, например список,
в данном случае к изменяемому типу в переменной immutable_var относится
[1, 2, 3], который является списком и может быть изменен.'''
mutable_lst  = immutable_var[4]
mutable_lst[1]= 'True'
mutable_lst[0] = False
mutable_lst[2] = 4
print(mutable_lst)
