class block():
    def __init__(self, name, teacher, info):
        self.name = name
        self.teacher = teacher
        self.info = info

class schedule():
    def __init__(self, student, blocks, gradeLevel, assembly):
        self.student = student
        self.blocks = blocks
        self.gradeLevel = gradeLevel
        self.assembly = assembly

    def giveBlockInformation(self, block):
            ##### Input block letter
            blockDic = {
                "A": 0,
                "B": 1,
                "C": 2,
                "D": 3,
                "E": 4,
                "F": 5,
                "G": 6,
                "H": 7,
                "I": 8,  
            }
            block = block.upper()
            b = blockDic.get(block)
            return self.blocks[b].info   
             