import unittest

from modules.BinaryOperator import BinaryOperatorClass

class Testing(unittest.TestCase):
    def Missing_Filetest(self):
        BinaryOperatorClass("./test.txt") 
        self.assertRaises(FileNotFoundError)
    def Read_From_Filetest(self):
        file = open("./test.txt","w")
        file.write("Hello There \n")
        file.close()
        TestObject = BinaryOperatorClass("./test.txt") 
        self.assertAlmostEqual(TestObject.data,b"Hello There \n")
    

