import pytest
import unittest
from pizza import pizza
class test_PizzaCreator(unittest.testCase):
    def test_pizzaName(self):
        piz = new.pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.type, "Classic")
    def test_pizzaTomato(self):
        piz = new.pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.tomato, True)
    def test_pizzaCheese(self):
        piz = new.pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.cheese, ["Mozarella", "Parmesan"])
    def test_pizzaStuffed(self):
        piz = new.pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.stuffed, False)
    def test_PizzaToppings(self):
        piz = new.pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.toppings, [])
    def test_PizzaBake(self):
        piz = new.pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        piz.bake()
        self.assertEqual(piz.baked, True)
    def test_PizzaNotBake(self):
        piz = new.pizza("Clasic", True, ["Mozarella", "Parmesan"], False, [])
        self.assertEqual(piz.baked, False)

