# Dictionary. Store data as "key: value" pairs. Mutable. Keys must be unique.

# Define like this.
my_dict = {}
another_my_dict = dict()

# You can create it populated.
user_info: dict = {
    "name": "Bruce",
    "age": 35,
    "married": True,
}

print(f"{user_info=}")

# Get value by key:
name = user_info["name"]
print(f"{name=}")

print(f"{user_info=}")

# Add keys:
user_info["hobbies"] = [
    "Programming",
    "Running",
]

print(f"{user_info=}")

# Change values by keys:
user_info["age"] += 10
print(f"{user_info=}")

# Create new dict, by merging with another dict:
another_info = {
    "age": 17,
    "nickname": "Batman",
}
new_info = user_info | another_info
print(f"{user_info=}, {another_info=}")
print(f"{new_info=}")

# Update values by other dict:
user_info.update(another_info)
print(f"{user_info=}, {another_info=}")

# Delete key with value:
del user_info["hobbies"]

print(f"{user_info=}")
