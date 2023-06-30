# Object, Class, Instance.
#
# Object is as box.
#   It can contain:
#   - "variables" (called "attributes")
#   - "functions" (called "methods") for work with this variables.
#
# Class is as "custom type". As int, str, etc. In general, class is as blueprint for creating objects.
#
# Instance for "class" is an "object", created by this "class".

class SayMixin:
    def say(self) -> str:
        return f"Hi, i am {self.name}. I'm {self.age} old."


class BlaBase:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bla = 1

    @property
    def bla(self):
        return self._bla

    @bla.setter
    def bla(self, value):
        self._bla = value

    @bla.deleter
    def bla(self):
        del self._bla


class HumanClass(SayMixin, BlaBase):
    # This method used to initialize values of "instance"
    def __init__(self, name: str, age: int = 18, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.age = age

    # This method use attributes from "instance"

    def change_age(self, new_age: int) -> None:
        self.age = new_age


def make_actions(human_instance: HumanClass) -> None:
    print(human_instance.say())
    print(human_instance.name)
    print(type(human_instance))

    human_instance.change_age(new_age=23)
    print(human_instance.say())


class Heart:
    pass


class Human:
    def __init__(self, ):
        self.heart = Heart()


# Human().heart

class Door:
    pass


class Room:
    def __init__(self, door: Door):
        self.door = door


# door = Door()
# room = Room(door=door)
# del door

if __name__ == "__main__":
    aleks = HumanClass(name="Aleks")
    make_actions(human_instance=aleks)
