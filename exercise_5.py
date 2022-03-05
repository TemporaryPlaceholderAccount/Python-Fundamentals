Morally_bankrupt = 'Nestle'
print("Is Nestle morally bankrupt? I predict True.")
print(Morally_bankrupt == 'Nestle')

canada = "I am warm when the weather gets warmer"
print("Will I get warm when it gets warmer'? I predict True.")
print(canada == 'I am warm when the weather gets warmer')

grape = "They did surgery on a grape"
print("Did they do surgery on a grape doh? I think so.")
print(grape == "They did surgery on a grape")

true = "evergy is a monopoly"
print("Is Evergy a local monopoly? Duh.")
print(true == "evergy is a monopoly")

big_num = "7 * 34"
print("Is '7 * 34' = 238? I predict True.")
print(big_num == "7 * 34")

heysoos = "I can walk on water"
print("Can I walk on water? Probably not.")
print(heysoos == "I can't walk on water")

ducky = 'The rubber duck is unhelpful/creepy'
print("Is ducky creepy? This is mean and slander and false.")
print(ducky == 'The rubber duck is VERY helpful')

UMU = "Programmer socks don't improve coding skills"
print("I felt bad about making you grade this so late, so I put in a meme you might have to think about. I predict false.")
print(UMU == "This is a skill based game")

blasephemy = 'coding isnt fun'
print("Is coding unfun? I don't think so.")
print(blasephemy == 'coding is fun')

no = 'Jeffery epstien killed himself'
print("Did Jeffery epstien killed himself'? We shall ask the machine, I predict false.")
print(no == 'Jeffery epstien has already been forgotten by the majority of people') 

# equality and inequality the '==' *
car = 'BMW'
print(car == 'BMW')

car = 'BMW'
print(car == 'subaru')

#lower, the .lower() *
car = 'SUBARU'
print(car)
print(car.lower())
    
if car.lower() == "subaru":
    print("Equal")

#is it on the list?
car = ['subaru', 'honda', 'chevy', 'ford']
if 'chevy' in car:
    print("true")

car = ['subaru', 'honda', 'chevy', 'ford']
if 'corvette' in car:
    print("true")

#captain, his name's not on the list!
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(user.title() + "True")

banned_users = ['andrew', 'carolina', 'david']
user = 'andrew'
if user not in banned_users:
 print(user.title() + "True")