import pytest
import unittest
from makeClasses import person
class test_personClasses(unittest.TestCase):
    #Test correct creation of the class
    def testCreationName(self):
        self.assertEqual(person('Peter','1.1.2001', 'No Hair', 'Helicopter').name, 'Peter', 'The name seems wrong')
    
    def testCreationBirthday(self):
        self.assertEqual(person('Peter','1.1.2001', 'No Hair', 'Helicopter').birthday, '1.1.2001', 'The birthday seems wrong')
    
    def testCreationHair(self):
        self.assertEqual(person('Peter','1.1.2001', 'No Hair', 'Helicopter').hair, 'No Hair', 'The hair color seems wrong')
       
    def testCreationGender(self):
        self.assertEqual(person('Peter','1.1.2001', 'No Hair', 'Helicopter').gender, 'Helicopter', 'The gender seems wrong')

    def testNameChange(self):
        pers = person('Peter','1.1.2001', 'No Hair', 'Helicopter')
        pers.changeName('Peter Parker')
        self.assertEqual(pers.name, 'Peter Parker', 'Changing the name seems not to work')
    
    def testHairChange(self):
        pers = person('Peter','1.1.2001', 'No Hair', 'Helicopter')
        pers.changeHair('Brown')
        self.assertEqual(pers.hair, 'Brown', 'Changing the hair seems not to work')