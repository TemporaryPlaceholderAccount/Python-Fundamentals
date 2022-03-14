#9-6
class Restaurant():

    def __init__(self, name, food):
        self.name = name.title()
        self.food = food

    def describe_restaurant(self):
        msg = self.name + " serves great " + self.food + "."
        print(msg)

    def open_restaurant(self):
        msg = self.name + " We're open! Come on in!"
        print(msg)

class IceCreamStand(Restaurant):
    def __init__(self, name, food='ice_cream'):
        super().__init__(name, food)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand('Big Boy Borgar')
big_one.flavors = ['vanilla', 'chocolate', 'strawberry', 'mocha', 'rocky road', 'sherbert', 'froyo\n']

big_one.describe_restaurant()
big_one.show_flavors()

#9-7
class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print(self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

josh = User('josh', 'matches', 'ematches', '123@example.com', 'void')
josh.describe_user()
josh.greet_user()

willie = User('willie', 'burger', 'wburger', '321@example.com', 'void')
willie.describe_user()
willie.greet_user()

class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)

        self.privileges = Privileges()

#9-8
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nUser's privileges: \n")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)

josh = Admin('josh', 'matches', 'ematches', '123@example.com', 'void')
josh.describe_user()

josh.privileges.show_privileges()

josh.privileges = [
    'can message users',
    'can moderate posts',
    'can delete accounts',
    'can evade the law',
    ]

josh.privileges.show_privileges()
#i couldn't get this to work. Nobody I asked seem to ever know how to fix.
#im lost