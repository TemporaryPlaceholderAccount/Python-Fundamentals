#5-8
usernames = ['admin', 'asdf', '1234', 'fdsa', '4321']
for username in usernames:
    if username == 'admin':
         print("Hello admin, would you like to see a status report?")
    else:
         print("Hello " + username + ", " "thank you for logging on again!")

#5-9
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
         print("Hello admin, would you like to see a status report?")
    else:
         print("Hello " + username + ", " "thank you for logging on again!")
else:
    print("We need to find some users!")


#5-10
current_users = ['yhn', 'ujm', 'ik,', 'olk', 'rfv', 'tgb']

new_users = ['yhn', 'ujm', 'ik,', 'olk', 'rfv', 'tgb']
for new_user in new_users:
    if new_users in current_users:
         print("Username available")
    else:
        print("Username unavailable")

#5-11
ordinals = list(range(1,10))

for ordinal in ordinals:
  if ordinal == 1:
     print("1st")
  elif ordinal == 2:
     print("2nd")
  elif ordinal == 3:
     print("3rd")
  else:
     print(str(ordinal) + "th")

#6-1
Mike_Ike = {
    'firstname': 'Mike',
    'lastname': 'Ike',
    'age': '21',
    'city': 'Wichita',
    }

print(Mike_Ike['firstname'])
print(Mike_Ike['lastname'])
print(Mike_Ike['age'])
print(Mike_Ike['city'])

#6-7
kyle_kyntronos = {
    'firstname': 'kyle',
    'lastname': 'kyntronos',
    'age': '20',
    'city': 'Wichita',
    }

seth_engles = {
    'firstname': 'seth',
    'lastname': 'engles',
    'age': '21',
    'city': 'Wichita',
    }

frens = [Mike_Ike, kyle_kyntronos, seth_engles]
print(frens)