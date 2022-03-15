try:
    a = input("First number: ")
    a = int(a)

    b = input("Second number: ")
    b = int(b)

except ValueError: 
    print("I'm sorry, I really do need a number")

else:
    sum = a + b
    print("= " + str(sum))
#10-7
while True:
    try:
        a = input("\nGive me a number: ")
        if a == 'q':
            break

        a = int(a)

        b = input("Give me another number: ")
        if b == 'q':
            break

        b = int(b)

    except ValueError: 
        print("I'm sorry, I really did need a number")

    else:
        sum = a + b
        print("= " + str(sum))

        #10-8
filenames = ['cat.tcl', 'dog.txt']

for filename in filenames:

    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("Sorry, file not found.")

#10-9
filenames = ['cat.tcl', 'dog.txt']

for filename in filenames:

    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
           print(contents)