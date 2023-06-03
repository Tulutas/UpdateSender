import unittest
import os 
from modules.BinaryOperator import BinaryOperatorClass

class Testing(unittest.TestCase):
    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            BinaryOperatorClass("./NotAFile.txt")
    def test_read_from_file(self):
        file = open("./test.txt","w")
        file.write("Hello There")
        file.close()
        TestObject = BinaryOperatorClass("./test.txt") 
        self.assertEqual(TestObject.data,b"Hello There")
        if os.path.exists("./test.txt"):
            os.remove("./test.txt")


    
