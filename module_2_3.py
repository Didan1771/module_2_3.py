
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
numbers_posit = []
a = 0
while a < len(my_list):
    number = my_list[a]
    if number < 0:
        break
    if number > 0:
        numbers_posit.append(number)
    a += 1
print(numbers_posit)





