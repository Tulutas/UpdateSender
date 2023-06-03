import unittest
import os 
from modules.TCPOperator import TCPClass

class Testing(unittest.TestCase):
    def test_server_echo(self):
       TCPObject= TCPClass("127.0.0.1",30000)
       TCPObject.open_tcp_server()
       


    
