import pytest
from dictionaries import translate
import unittest
class test_dictionaryPhonebook(unittest.TestCase):
    def test_Jack(self):
        self.assertEqual(translate("Jack"), "012314243423", "Make sure that you return the number as a string")
    def test_Tom(self):
        self.assertEqual(translate("Tom"),"012314234323432")
    def test_AnotherPerson(self):
        self.assertEqual(translate("AnotherPerson"),"01231474747")
    def test_Epty(self):
        self.assertEqual(translate(""), None)