#5-3
alien_colorG = "green"

if alien_colorG is "green":
    print("5 Points!")
  
if alien_colorG is "red":
    print("5 Points!")

#5-4
alien_colorY = "yellow"

if alien_colorG is "green":
    print("5 Points!")
else: 
    print("10 Points!")

if alien_colorY is "green":
    print("5 Points!")
else: 
    print("10 Points!")

#5-5
alien_colorR = "red"

if alien_colorG is "green":
 print("5 Points!")

elif alien_colorG is "yellow":
 print("10 Points!")

else:
 print("15 Points!")

if alien_colorY is "green":
 print("5 Points!")

elif alien_colorY is "yellow":
 print("10 Points!")

else:
 print("15 Points!")

if alien_colorR is "green":
 print("5 Points!")

elif alien_colorR is "yellow":
 print("10 Points!")

else:
 print("15 Points!")

#5-6
age = 12

if age < 2:
 print("You are an infant")
elif age < 4:
 print("You are a toddler")
elif age < 13:
 print("You are a kid")
elif age < 20:
 print("You are a teenager")
elif age < 65:
 print("You are an adult")
else:
 print("You are an elder")

#5-7 bool

def funky():
    print(bool("works"))
#the name of the argument is "works" as I was not given the "below values". it is true because a boolean is either 1 or 0, so the boolean will return true as it is not empty
funky()