#8-15, also import of 8-16
import printing_functions

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

#8-16

from printing_functions import print_models
from printing_functions import print_models as fn
import printing_functions as mn
from printing_functions import *

#9-10
import food_place

food_place.Big_Boy_Borgar=food_place.IceCreamStand('Big Boy Borgar')
food_place.Big_Boy_Borgar.flavors = ['vanilla', 'chocolate', 'strawberry', 'mocha', 'rocky road', 'sherbert', 'froyo\n']

#9-11
import all3

from all3 import Admin

#i'm having issues with the repository, i think i might have gunked it up with too many files.

josh = all3.Admin('josh', 'matches', 'ematches', '123@example.com', 'void')
all3.josh.describe.user()

josh.privileges = [
    'can message users',
    'can moderate posts',
    'can delete accounts',
    'can evade the law',
    ]

all3.josh.privileges.show_privileges()

#9-12
from user import User
from admin import Admin


josh = Admin('josh', 'matches', 'ematches', '123@example.com', 'void')
admin.Admin.josh.describe.user()
admin.josh.privileges.show_privileges()

#It would seem my issue with the repository continues. Nothing i try seems to work, and none of my classmates have an answer to my predicament.