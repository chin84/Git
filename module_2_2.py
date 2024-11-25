first, second, third = int(input()), int(input()), int(input())
if first == second and second == third:
    print(3)
elif (first == third and second != third) or (first == second and second != third) or (first != third and second == third):
    print(2)
else:
    print(0)
