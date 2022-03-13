class Guitar:
    def __init__(self, Number_of_strings, Acoustic, Made_of_wood):
        self.Number_of_strings = Number_of_strings
        self.Acoustic = Acoustic
        self.Made_of_wood = Made_of_wood

    def horse_start_stop(self):
        print(str.format("Does {0} it work", self.Made_of_wood))

    @property
    def Number_of_strings(self):
        return self.Number_of_strings

    @Number_of_strings.setter
    def Number_of_strings(self, bre):
        self.Number_of_strings = bre

    @property
    def Acoustic(self):
        return self.Acoustic

    @Acoustic.setter
    def Acoustic(self, run):
        self.Acoustic = run

    @property
    def Made_of_wood_type(self):
        return self.Made_of_wood_type

    @Made_of_wood_type.setter
    def Made_of_wood_type(self, Made_of_wood):
        self.Made_of_wood_type = Made_of_wood

my_horse = Guitar("9", 100000000000000000000000000, "yes")
print(my_horse.Made_of_wood)
print(my_horse.horse_start_stop)
