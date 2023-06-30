# Don't change list, while iterate over it. Because you can have problems.

lemon = "Lemon"

fruits = ["Kiwi", "Apple", "Pineapple", lemon, "Pineapple"]
for fruit in fruits:
    if fruit == lemon:
        fruits.insert(1, "Mango")
    print(f"{fruit}, {fruits}")

    if len(fruits) >= 10:
        break

print(f"{fruits=}")
