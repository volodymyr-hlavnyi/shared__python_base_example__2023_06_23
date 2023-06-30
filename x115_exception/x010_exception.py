def make_action(number):
    try:
        print("Before action")
        # noinspection PyStatementEffect
        2 / number
        print("After action")
    except ZeroDivisionError:
        print("Inside of handling")
    else:
        print("else")
    finally:
        print("finally")

    print("===")


make_action(10)
make_action(0)

# noinspection PyTypeChecker
make_action("Hello")
