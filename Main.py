

from modules.TCPOperator import TCPClass
from modules.BinaryOperator import BinaryOperatorClass
import time 

newobject=TCPClass("127.0.0.1",30002)
newobject.open_tcp_socket()

#newobject.start_echo_listening()
data=b'\x00\x01\x02\x03\x04'
newobject.connect_to_server("127.0.0.1",35000)


DataObject=BinaryOperatorClass("./data/test.hex")
data_to_sended= DataObject.Read()

newobject.send_data_to_all(data_to_sended)

time.sleep(1000)