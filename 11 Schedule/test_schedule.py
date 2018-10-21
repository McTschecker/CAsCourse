import pytest	
import unittest	
from schedule import block, schedule	
 ### Helper	
def blockCreator():	
    blocks = []	
    blockA = block("Econ", "Padula", "Very Fun")	
    for i in range(10):	
        blocks += blockA	
    return blocks	
class test_block(unittest.TestCase):	
    def test_blockCreationName(self):	
        blockA = block("Econ", "Padula", "Very Fun")	
        self.assertEqual(blockA.name, "Econ")	
    def test_blockCreationTeacher(self):	
        blockA = block("Econ", "Padula", "Very Fun")	
        self.assertEqual(blockA.teacher, "Padula")	
    def test_blockCreationInfo(self):	
        blockA = block("Econ", "Padula", "Very Fun")	
        self.assertEqual(blockA.info, "Very Fun")	
 class test_schedule(unittest.TestCase):	
    def test_scheduleCreationStudent(self):	
        scheduleA = schedule('Max Mustermann', blockCreator(), "Wendnesday", "Thursday")	
        self.assertEqual(scheduleA.student, "Max Mustermann")	
    def test_scheduleCreationBlocks(self):	
        scheduleA = schedule('Max Mustermann', blockCreator(), "Wendnesday", "Thursday")	
        self.assertEqual(scheduleA.blocks, blockCreator())	
    def test_scheduleCreationGradeLevel(self):	
        scheduleA = schedule('Max Mustermann', blockCreator(), "Wendnesday", "Thursday")	
        self.assertEqual(scheduleA.gradeLevel, "Wendnesday")	
    def test_scheduleCreationAssembly(self):	
        scheduleA = schedule('Max Mustermann', blockCreator(), "Wendnesday", "Thursday")	
        self.assertEqual(scheduleA.assembly, "Thursday")