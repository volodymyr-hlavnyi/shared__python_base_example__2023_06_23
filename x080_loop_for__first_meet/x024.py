my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list_2 = [item ** 2 for item in my_list if item % 2 == 0]

my_list_2 = []
for item in my_list:
    if item % 2 == 0:
        my_list_2.append(item ** 2)
