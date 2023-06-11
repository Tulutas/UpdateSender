

from modules.TCPOperator import TCPClass
from modules.BinaryOperator import BinaryOperatorClass
import time 

newobject=TCPClass("192.168.1.131",30002)
newobject.open_tcp_socket()

#newobject.start_echo_listening()
data=b'\x00\x01\x02\x03\x04'
newobject.connect_to_server("192.168.1.116",3500)


DataObject=BinaryOperatorClass("./data/oakbati.hex")
data_to_sended= DataObject.Read()   
data_to_send=DataObject.ReadDatalines()

i=0
process=True
while process: 
    if 4*i<len(data_to_send):
        newobject.send_data_to_all(data_to_send[4*i])
        newobject.send_data_to_all(data_to_send[4*i+1])
        newobject.send_data_to_all(data_to_send[4*i+2])
        newobject.send_data_to_all(data_to_send[4*i+3])
    else:
        break
    i=i+1
    time.sleep(1000)
time.sleep(1000)