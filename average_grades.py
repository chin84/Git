grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
lst_students = sorted(list(students))
print(lst_students)
dict_students_and_grades = {}
dict_students_and_grades.update({lst_students[0]: sum(grades[2])/len(grades[2]),
                                lst_students[1]: sum(grades[1])/len(grades[1]),
                                lst_students[2]: sum(grades[2])/len(grades[2]),
                                lst_students[3]: sum(grades[3]) / len(grades[3]),
                                lst_students[4]: sum(grades[4])/len(grades[4])})
print('Средние оценки студентов: ', dict_students_and_grades)
