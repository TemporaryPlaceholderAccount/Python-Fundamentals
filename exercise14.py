from city_functions import local
import unittest

#11-1 the file gave me a headache, but alls well that ends well.

class PlaceTestCase(unittest.TestCase):

    def test_local(self):
        santiago_chile = local('Santiago', 'Chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_local_population(self):
        santiago_chile = local('Santiago', 'Chile', population=5000000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')


unittest.main()


from employee import Employee

class Testwagie(unittest.TestCase):
    def setUp(self):
        self.li = Employee("Dick", "Johnson", 5000)

    def test_give_default_raise(self):
        self.li.give_raise()
        self.assertEqual(self.li.salary, 5000)

    def test_give_custom_raise(self):
        self.li.give_rise(5000)
        self.assertEqual(self.li.salary, 5000)

unittest.main()