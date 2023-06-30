# With "for" loop you can "iterate" over any "iterable". For example, over string.

my_string = "Hello world"

for character in my_string:
    print(character)

for index in range(len(my_string)):
    character = my_string[index]
    print(character)

for index, character in enumerate(my_string):
    print(index, character)

for index, character in enumerate(my_string, start=1):
    print(index, character)
