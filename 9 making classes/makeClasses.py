class person:
    def __init__(self, name, birthday, hair, gender):
            self.name = name
            self.birthday = birthday
            self.hair = hair
            self.gender = gender
    def changeName(self, newName):
        self.name = newName
    def changeHair(self, newHair):
        self.hair = newHair
