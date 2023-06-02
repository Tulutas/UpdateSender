import unittest
from BinaryOperator import BinaryOperatorClass

class testBinary(unittest.TestCase):
    def Missing_Filetest(self):
        TestObject = BinaryOperatorClass("./test.txt") 
        self.assertRaises(FileNotFoundError)
    def Read_From_Filetest(self):
        file = open("./test.txt","w")
        file.write("Hello There \n")
        file.close()
        TestObject = BinaryOperatorClass("./test.txt") 
        self.assertAlmostEqual(TestObject.data,b"Hello There \n")
    
if __name__ == '__main__':
    unittest.main()
    test=testBinary()
    test.Missing_Filetest()
    test.Read_From_Filetest()