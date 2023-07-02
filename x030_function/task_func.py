
def my_function(name :str ='Volodymyr', number1: int = 1, number2: int = 2):
    sum = number1 + number2
    return f'String {name=} and sum {number1=} and {number2=} equal {sum}'

print(f'1st use default {my_function()}')

#name = input('Enter string value: ')
#number1 = int(input('Enter number 1: '))
#number2 = int(input('Enter number 2: '))

#print(f'2nd use w parameters {my_function(name,number1,number2)}')

def func(number: int, my_list: list[int] = None):
    if my_list is None:
        my_list = []

    my_list.append(number)
    return my_list


some_list = []
print(func(1,some_list))
print(func(3,some_list))


print(func(2, some_list))
some_list.append(4)
print(some_list)