this_is_true = True
this_is_false = False

print(f"{this_is_true=}, {type(this_is_true)}")
print(f"{this_is_false=}, {type(this_is_false)}")

print(f"not True: {not True}")
print(f"not False: {not False}")

print(f"2 > 3: {2 > 3}")
print(f"2 == 2: {2 == 2}")
print(f"2 != 3: {2 != 3}")

print(f"(2 == 2) and (2 > 3): {(2 == 2) and (2 > 3)}")
print(f"(2 == 2) or (2 > 3): {(2 == 2) or (2 > 3)}")

a = 10
b = 1
print(f"2 < {a} < 20: {2 < a < 20}")
print(f"2 < {b} < 20: {2 < b < 20}")

string = "NOTEbook"
second_string = "noteBOOK"
print(f"{string} == {second_string}: {string == second_string}")
print(
    f"{string.lower()} == {second_string.lower()}: {string.lower() == second_string.lower()}"
)
