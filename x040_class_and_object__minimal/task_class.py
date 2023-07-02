class Computer:
    def __init__(self, name:str, hdd:int ,ram:int):
        self.hdd = hdd
        self.ram = ram
        self.name = name
    def __str__(self):
        return f'Computer {self.name}, HDD {self.hdd}, RAM {self.ram}'

my_nootebook = Computer(name='Dell', hdd=1000, ram=16)
print(my_nootebook)