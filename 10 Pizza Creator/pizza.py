class pizza():
    def __init__(self, type, tomato, cheese, stuffed, toppings):
        self.type = type
        self.tomato = tomato
        self.cheese = cheese
        self.stuffed = stuffed
        self.toppings = toppings
        self.baked = False
    def bake(self):
        self.baked = True
    