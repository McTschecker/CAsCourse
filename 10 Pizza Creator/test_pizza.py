import pytest
import unittest
from pizza import pizza
class test_PizzaCreator(unittest.TestCase):
    def test_pizzaName(self):
        piz = pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.type, "Classic")
    def test_pizzaTomato(self):
        piz = pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.tomato, True)
    def test_pizzaCheese(self):
        piz = pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.cheese, ["Mozarella", "Parmesan"])
    def test_pizzaStuffed(self):
        piz = pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.stuffed, False)
    def test_PizzaToppings(self):
        piz = pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.toppings, [])
    def test_PizzaBake(self):
        piz = pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        piz.bake()
        self.assertEqual(piz.baked, True)
    def test_PizzaNotBake(self):
        piz = pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.baked, False)
