#8-3
def make_shirt(message, size): 
    print("A "+ size + " shirt with " + message + " written on its back.")
    
make_shirt("I love Python", "large")
make_shirt(size = "large", message = "I love Python")

#8-4
def make_shirt(message, size = "large"): 
    print("A "+ size + " shirt with " + message + " written on its back.")
    
make_shirt("I love Python", size =  "medium")
make_shirt("I hate my job")

#8-5
def describe_city(city, country = "Italy"):
    print(city + " is the capital of " + country)

describe_city("Rome")
describe_city("Reykjavik")
describe_city("Wichita")

#8-9
magicians = ["Neil Harris", "Penn Jillette", "Harry Houdini", "Raymon Teller"]

def show_magicians(magicians):
    print(magicians)

show_magicians(magicians)

#8-10
magicians = ["Neil Harris", "Penn Jillette", "Harry Houdini", "Raymon Teller"]
the_greats2 = []

def show_magicians(magicians):
    print(magicians)

def make_great(magicians):
    while magicians:
        magician = magicians.pop()
        great = magician + " the Great"
        the_the_greats2.append(great)
    for great in the_the_greats2:
        print(great.title())

make_great(magicians)
show_magicians(magicians)
#8-11
#I was largely unsure of what the assignment was actually asking for. It seems like a convaluted request to print another list, but I feel I was having trouble understanding it.
magicians2 = ["Neil Harris", "Penn Jillette", "Harry Houdini", "Raymon Teller"]
the_greats2 = []

def make_great(magicians2):
    while magicians2:
        magician_copy = magicians2.pop()
        great = magician_copy + " the Great"
        the_greats2.append(great)
    for great in the_greats2:
        magicians.append(the_greats2)
        print(great.title())
    return magicians

make_great(magicians2)
show_magicians(magicians2)

#9-1



#9-2



#9-3