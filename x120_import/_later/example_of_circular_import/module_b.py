import module_a  # this is a circular import of module_a


def print_available_local_modules():
    """
    This is supportive function that prints a list of local modules
    which are available from sys at current moment.
    :return:
    """
    import sys

    local_added_modules = [m for m in sys.modules.keys() if m.startswith("module")]
    print(f"local_added_modules: {local_added_modules}")


print("this point is a start of module b")

print_available_local_modules()

print("this is a point before creating variable 'first_string_in_module_b'")
first_string_in_module_b = "first_string_in_module_b"
second_string_in_module_b = "second_string_in_module_b"
print("this is a point after creating variable 'first_string_in_module_b'")
print(module_a.first_string_in_module_a)
print("this point is an end of module b")
# noinspection PyUnresolvedReferences
module_a.new_func()
