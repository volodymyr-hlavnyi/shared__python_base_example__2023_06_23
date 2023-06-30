# You can use extra control for your loop.
#   - "continue" operator: Go to next iteration now
#   - "break" operator: Stop loop now
#   - "else" block: Executed, if not used "break".


def make_output(string):
    break_at = "7"
    continue_at = "3"
    print(f"String: {string}. {continue_at=}, {break_at=}")

    for character in string:
        if character == continue_at:
            print("continue")
            continue
        elif character == break_at:
            print("break")
            break

        print(character)
    else:
        print("else")

    print("===")


my_string = "0123456789"
my_another_string = "012345"
my_empty_string = ""

make_output(my_string)
make_output(my_another_string)
make_output(my_empty_string)
