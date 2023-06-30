import random

from my_module import imported_value
from package import another_module

print("Main. Output 1")
print(f"{__name__=}")

if __name__ == "__main__":
    print("Main. Output 2")

    print(f"{imported_value=}")
    print(f"{another_module.another_imported_value=}")
    print(f"{random.randint(0,10)=}")
