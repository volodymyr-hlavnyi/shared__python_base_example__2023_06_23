import module_a

if __name__ == "__main__":
    print("this point is a start of main")

    def print_available_local_modules():
        """
        This is supportive function that prints a list of local modules
        which are available from sys at current moment.
        :return:
        """
        import sys

        local_added_modules = [m for m in sys.modules.keys() if m.startswith("module")]
        print(f"local_added_modules: {local_added_modules}")

    # When Python imports a module, it first checks
    # the module registry (sys.modules) to see if the module is already imported.
    # If that’s the case, Python uses the existing module object as is.

    # For getting example of a circular import error run main.py

    print_available_local_modules()
    print(
        f"this is imported string from module_a: {module_a.second_string_in_module_a}"
    )
    print("this point is a end of main")
