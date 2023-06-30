# List is a ordered mutable sequence of values.

# Define like this.
my_list = []
another_my_list = list()  # sourcery skip: list-literal

# You can make list from string
my_string = "Hello world"
string_as_list = list(my_string)
print(f"{my_string=}")
print(f"{string_as_list=}")

# You can create it populated.
fruits: list[str] = ["Kiwi", "Apple", "Lemon", "Pineapple"]
print(fruits)

# You can fill list.
# Add item in the end.
fruits.append("Cherry")
print(fruits)
# Add few items in the end.
fruits.extend(["Orange", "Tomato"])
print(fruits)

# Get and delete from list last item
popped_last = fruits.pop()
print(fruits)
print(f"{popped_last=}")

# Delete item by this item:
fruits.remove("Kiwi")
print(fruits)

# Sort items
fruits.sort()
print(fruits)

# Check existence:
lemon = "Lemon"
print(f'Is "{lemon}" in collection? {lemon in fruits}')
lemon_lower = lemon.lower()
print(f'Is "{lemon_lower}" in collection? {lemon_lower in fruits}')

# Iterate over it:
for fruit in fruits:
    print(fruit)
print(fruits)

# Delete all items
fruits.clear()
print(fruits)
