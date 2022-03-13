class Horse:
    def __init__(self, Length_of_hair, Gender, Age):
        self.Length_of_hair = Length_of_hair
        self.Gender = Gender
        self.Age = Age

    def horse_start_stop(self):
        print(str.format("Does {0} it work", self.Age))

    @property
    def Length_of_hair(self):
        return self.Length_of_hair

    @Length_of_hair.setter
    def Length_of_hair(self, bre):
        self.Length_of_hair = bre

    @property
    def Gender(self):
        return self.Gender

    @Gender.setter
    def Gender(self, run):
        self.Gender = run

    @property
    def Age_type(self):
        return self.Age_type

    @Age_type.setter
    def Age_type(self, Age):
        self.Age_type = Age

my_horse = Horse("Long", 1, "Colt")
print(my_horse.Age)
print(my_horse.horse_start_stop)