def func(number: int, my_list: list[int] = None):
    if my_list is None:
        my_list = []

    my_list.append(number)
    return my_list



print(func(1))
print(func(3))

some_list = []
print(func(2, some_list))
some_list.append(4)

