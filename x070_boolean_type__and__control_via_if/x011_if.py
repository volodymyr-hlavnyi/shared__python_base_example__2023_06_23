# With if-elif-else you can control flow of execution.


def make_decision(number):
    if number == 7:
        return f"{number} Equal 7"
    elif number >= 20:
        return f"{number} bigger then 20"
    elif number != 5:
        return f"{number} not equal 5"
    else:
        return "Else"


print(make_decision(7))
print(make_decision(25))
print(make_decision(8))
print(make_decision(5))
