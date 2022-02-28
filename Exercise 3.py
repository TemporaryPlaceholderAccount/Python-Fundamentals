john = "John"

print("It's been so long since i last saw " + john + "!")

print(john.lower() + ", " + john.upper() + ", " + john.title())

print('Genghis Khan once said, "The strength of the walls depends on the courage of those who guard them."')

famous_person = "Genghis Khan"

message =  'once said, "The strength of the walls depends on the courage of those who guard them."'

print(famous_person + " " + message)

ws_name = " \t\nsmitty wettermenjenson\n "

print(ws_name)

#for some reason, the whitespace doesnt seem to want to print. everything else is working fine though

print(ws_name.lstrip())
print(ws_name.rstrip())
print(ws_name.strip())