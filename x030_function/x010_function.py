# Function allow you to group some actions together.

# At first, you define function. It not executed now.
def hello_function():
    print("Hello from function")


# Then, you need to "call" it.
hello_function()


# So, "print" is just a "built-in function"

# Also, function can have "value to return".
def hello_function_with_return():
    return "Hello from function with return"


# You can assign this value to variable, or send it directly to another function.
output = hello_function_with_return()
print(output)

print(hello_function_with_return())

# Better if one function created for one purpose.
#   For example, one for calculation, another for output.
#   Thanks to this, you can change how you output your data. To the console, to a file, or something else.

# "Function" naming convention:
#   - as variable
