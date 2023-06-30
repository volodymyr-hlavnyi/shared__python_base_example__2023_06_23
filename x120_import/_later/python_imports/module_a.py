# noinspection PyUnresolvedReferences
from package_a import module_d
from module_b import int_module_b as b

if __name__ == "__main__":
    print("as main")
    # print(module_d.str_module_d_and_c)
    print(b)
