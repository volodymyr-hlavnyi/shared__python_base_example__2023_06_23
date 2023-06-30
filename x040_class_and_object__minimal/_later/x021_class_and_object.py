# Class is as "custom type".
# Class can create "instance of this class". Any instances of any classes we can call "object".
# In object can group "variables" (called "attributes") and "functions" (called "methods") for work with this variables.


class Human:
    # This method used to create "instance"
    def __init__(self, name: str):
        self.name = name

    # This method use attributes from "instance"
    def say(self) -> str:
        return f"Hi, i am {self.name}"

    def rename(self, new_name: str) -> None:
        self.name = new_name


if __name__ == "__main__":
    aleks = Human(name="Aleks")

    print(aleks.say())
    print(aleks.name)
    print(type(aleks))

    # In fact, all in Python is objects. "Class", "function", "string", is also objects.
    #   And they have "class", what create it.

    print(type(Human))
    print(type(Human.say))

    # "Class" naming convention:
    #   - as variable but in "CamelCase"
    #       Bad: "my_super_class"
    #       Good: "MySuperClass"
